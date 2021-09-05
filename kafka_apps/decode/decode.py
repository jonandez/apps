from kafka import KafkaConsumer
import binascii
import os
 

KAFKA_SERVER = os.getenv('KAFKA_SERVER', "172.16.16.150:9092")
INPUT_TOPIC  = os.getenv('INPUT_TOPIC', "output")

consumer = KafkaConsumer(bootstrap_servers=KAFKA_SERVER,
                        auto_offset_reset='latest',
                        value_deserializer=lambda v: binascii.unhexlify(v).decode('utf-8')
                        )
consumer.subscribe([INPUT_TOPIC])


for message in consumer:
    print(message.value)
