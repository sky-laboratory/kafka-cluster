from kafka import KafkaProducer
import json
import time


bootstrap_server = ["127.0.0.1:19092", "127.0.0.1:29092", "127.0.0.1:39092"]
TOPIC_NAME = "additional"

prod = KafkaProducer(bootstrap_servers=bootstrap_server)


j = 0 
for i in range(1, 11000):
    j += i 
    data = {"index": j}
    json_tf = json.dumps(data)    
    print(json_tf)
    prod.send(TOPIC_NAME, json_tf.encode("utf-8"))
    time.sleep(1)
    prod.flush()