from kafka import KafkaProducer
import time
import binascii
import os


KAFKA_SERVER = os.getenv('KAFKA_SERVER', "localhost:9092")
TOPIC_NAME = os.getenv('TOPIC_NAME', "input")


while(True):
    t = time.time()
    epoch_time = str(int(t))
    producer = KafkaProducer(value_serializer=lambda v: binascii.hexlify(v.encode('utf-8')), bootstrap_servers=KAFKA_SERVER)
    producer.send(TOPIC_NAME, epoch_time)
    producer.flush()