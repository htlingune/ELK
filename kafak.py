kafka-topics --list --zookeeper zookeeper:2181
kafka-topics --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic stock
