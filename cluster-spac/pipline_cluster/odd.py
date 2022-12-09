from kafka import KafkaConsumer
import json

TOPIC_NAME = "odd"
bootstrap_server = ["127.0.0.1:19092", "127.0.0.1:29092", "127.0.0.1:39092"]

consum = KafkaConsumer(TOPIC_NAME, bootstrap_servers=bootstrap_server)

for index in (json.loads(i.value.decode())["number"] for i in consum):
    print(index)