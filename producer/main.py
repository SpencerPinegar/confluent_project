from confluent_kafka import Producer
import random
import json

CONFIG = {
  'bootstrap.servers': 'pkc-12576z.us-west2.gcp.confluent.cloud:9092',
  'security.protocol': 'SASL_SSL',
  'sasl.mechanisms': 'PLAIN',
  'sasl.username': 'SPOSNJKWLEVGCLK6',
  'sasl.password': 'zx+qqus37IexKlrujshXjcD2OrpQ7AliXC17uiPJXsFgZ3o3v2IxpVDJ+kvK+bRO',
  # Best practice for higher availability in librdkafka clients prior to 1.7
  'session.timeout.ms': 45000
}

PRODUCT_LIST = ['item1', 'item2', 'item3', 'item4', 'item5']



def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def produce_order(producer):
    order = {
        'product': random.choice(PRODUCT_LIST),
        'quantity': random.randint(1, 10)
    }
    producer.produce('orders', value=json.dumps(order).encode('utf-8'), callback=delivery_report)
    producer.poll(0)
    producer.flush()

def main():
    producer = Producer(CONFIG)
    while True:
        produce_order(producer)

if __name__ == '__main__':
    main()