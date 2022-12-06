from kafka import KafkaConsumer
from kafka import KafkaProducer
import json


bootstrap_server = ["127.0.0.1:19092", "127.0.0.1:29092", "127.0.0.1:39092"]
TOPIC_NAME = "additional"
ODD_TOPIC = "odd"
EVEN_TOPIC = "even"


consum = KafkaConsumer(TOPIC_NAME, bootstrap_servers=bootstrap_server)
prod = KafkaProducer(bootstrap_servers=bootstrap_server)


def deliver_number(n: int) -> int:
    total = True if n % 2 == 0 else False
    return total


for index in (json.loads(i.value.decode())["index"] for i in consum):
    topic_trans = EVEN_TOPIC if deliver_number(index) else ODD_TOPIC
    msg = {"number": index}
    prod.send(topic_trans, value=json.dumps(msg).encode("utf-8"))
    print(topic_trans, deliver_number(index), index)
    prod.flush()
    
