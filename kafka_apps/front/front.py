from kafka import KafkaConsumer, KafkaProducer
from flask import Flask
import binascii
import os
 
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

KAFKA_SERVER = os.getenv('KAFKA_SERVER', "localhost:9092")
INPUT_TOPIC  = os.getenv('INPUT_TOPIC', "input")

@app.route('/')
def index():
    consumer = KafkaConsumer(bootstrap_servers=KAFKA_SERVER,
                            auto_offset_reset='latest',
                            # value_deserializer=lambda v: json.loads(v)
                            value_deserializer=lambda v: binascii.unhexlify(v).decode('utf-8')
                            )
    consumer.subscribe([INPUT_TOPIC])

    return render_template('index.html', message=consumer.message)


# for message in consumer:
#     print(message.value)

if __name__ == '__main__':
    app.run(port=80, debug=True, host='0.0.0.0')
