from confluent_kafka import Producer
import sys
import time
import requests
import json

def get_liveprice():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
    stocknumber = 2330
    query = 'http://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_{}.tw'.format(stocknumber)
    session = requests.session()
    response = requests.get(query, headers=headers)
    content = json.loads(response.text)
    return content

def error_cb(err):
    print('Error: %s' % err)

def delivery_callback(err, msg):
    if err:
        sys.stderr.write('%% Message failed delivery: %s\n' % err)
    else:
        if int(msg.key()) % 5 == 0:
            sys.stderr.write('%% Message delivered to topic:[{}]\n'.format(msg.topic()))

if __name__ == '__main__':
    props = {
        'bootstrap.servers': 'localhost:9092',
        'error_cb': error_cb,
        'retries' : '3'
        'max.in.flight.requests.per.connection' : '1'
    }
    producer = Producer(props)
    topicName = 'stock'
    try:
        content = get_liveprice()
        content = json.dumps(content.__dict__)
        while True:
            producer.produce(topicName, key=2330, value = content,callback=delivery_callback)
            producer.poll(0)
            print("good", end="\r")
            time.sleep(3)
        print('Send '  + ' messages to Kafka')
    except BufferError as e:
        sys.stderr.write('%% Local producer queue is full ({} messages awaiting delivery): try again\n'
                         .format(len(producer)))
    except Exception as e:
        print(e)
    producer.flush(5)
    print('Message sending completed!')