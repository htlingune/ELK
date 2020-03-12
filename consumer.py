from confluent_kafka import Consumer, KafkaException, KafkaError
import sys

def error_cb(err):
    print('Error: %s' % err)

def try_decode_utf8(data):
    if data:
        return data.decode('utf-8')
    else:
        return None

def my_assign(consumer_instance, partitions):
    for p in partitions:
        p.offset = 0
    print('assign', partitions)
    consumer_instance.assign(partitions)

if __name__ == '__main__':
    props = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'STUDENT_ID',
        'auto.offset.reset': 'earliest',
        'session.timeout.ms': 6000,
        'error_cb': error_cb
    }
    consumer = Consumer(props)
    topicName = "stock"
    consumer.subscribe([topicName], on_assign=my_assign)
    count = 0
    try:
        while True:
            records = consumer.consume(num_messages=1, timeout=1.0)
            if records is None:
                continue
            for record in records:
                if record is None:
                    continue
                if record.error():
                    if record.error().code() == KafkaError._PARTITION_EOF:
                        sys.stderr.write('%% {} [{}] reached end at offset {} - {}\n'.format(record.topic(), record.partition(), record.offset()))
                    else:
                        raise KafkaException(record.error())





'股票名稱' = content['msgArray'][0]['n']
'時間' = content['msgArray'][0]['t']
'昨日收盤價' = content['msgArray'][0]['y']
'開盤價' = content['msgArray'][0]['o']
'最高價' = content['msgArray'][0]['h']
'最低價' = content['msgArray'][0]['l']
'上市櫃' = content['msgArray'][0]['ex']
'最近成交價' = content['msgArray'][0]['z']
'最新交易成交張數' = content['msgArray'][0]['tv']
'當日成交量' = content['msgArray'][0]['v']
'五檔報價賣出價' = [i for i in content['msgArray'][0]['a'].split('_')][0:-1]
'五檔報價賣出量' = [i for i in content['msgArray'][0]['f'].split('_')][0:-1]
'五檔報價買入價' = [i for i in content['msgArray'][0]['b'].split('_')][0:-1]
'五檔報價買入量' = [i for i in content['msgArray'][0]['g'].split('_')][0:-1]
'漲停點' = content['msgArray'][0]['u']
'跌停點' = content['msgArray'][0]['w']