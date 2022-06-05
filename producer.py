# %%
import time
import argparse
import datetime
import json

from kafka import KafkaProducer

# %%
def make_kafka_producer(host_port):
    producer = KafkaProducer(bootstrap_servers=host_port, value_serializer = lambda x: json.dumps(x).encode('UTF-8'))
    return producer

# %%
def make_message(nr):
    msg = {
        'schema': {
            'type': 'struct',
            'fields': [
                {'type': 'int64', 'optional': False, 'field': 'timestamp'},
                {'type': 'int64', 'optional': False, 'field': 'nr'},
            ]
        },
        'payload': {
            'timestamp': int(datetime.datetime.utcnow().timestamp()),
            'nr': nr
        }
    }
    return msg

# %%
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('host_port', metavar='<hostname:port>', default='localhost:9092')
    parser.add_argument('--rate', type=float, default=5.0)
    parser.add_argument('--topic', default='dummy')
    args = parser.parse_args()
    
    producer = make_kafka_producer(args.host_port)

    i = 0
    while True:
        producer.send(args.topic, make_message(i))
        time.sleep(args.rate)
        i += 1

# %%
if __name__ == '__main__':
    main()



