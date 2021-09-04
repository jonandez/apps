from kafka import KafkaProducer, KafkaConsumer
import binascii
import os
import datetime

KAFKA_SERVER = os.getenv('KAFKA_SERVER', "localhost:9092")
INPUT_TOPIC = os.getenv('INPUT_TOPIC', "input")
OUTPUT_TOPIC = os.getenv('OUTPUT_TOPIC', "output")


consumer = KafkaConsumer(bootstrap_servers=KAFKA_SERVER,
                         auto_offset_reset='latest',
                        #  value_deserializer=lambda v: json.loads(v)
                         value_deserializer=lambda v: binascii.unhexlify(v).decode('utf-8')
                         )
consumer.subscribe([INPUT_TOPIC])


for message in consumer:
    epoch = datetime.datetime.fromtimestamp(int(message.value))
    iso_time = epoch.isoformat()
    producer = KafkaProducer(value_serializer=lambda v: binascii.hexlify(v.encode('utf-8')), bootstrap_servers=KAFKA_SERVER)
    producer.send(OUTPUT_TOPIC, iso_time)
    producer.flush()