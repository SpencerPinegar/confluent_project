import json
import os

from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.kafka import FlinkKafkaConsumer, FlinkKafkaProducer
from pyflink.common.serialization import SimpleStringSchema
from pyflink.common.typeinfo import Types
from pyflink.datastream.window import TumblingEventTimeWindows
from pyflink.common.time import Time



# Set up connection to remote JobManager
os.environ['PYFLINK_GATEWAY_PORT'] = '6122'  # Or any free port
os.environ['PYFLINK_GATEWAY_ADDRESS'] = 'jobmanager'

CONFIG = {
  'bootstrap.servers': 'pkc-12576z.us-west2.gcp.confluent.cloud:9092',
  'security.protocol': 'SASL_SSL',
  'sasl.mechanisms': 'PLAIN',
  'sasl.username': 'SPOSNJKWLEVGCLK6',
  'sasl.password': 'zx+qqus37IexKlrujshXjcD2OrpQ7AliXC17uiPJXsFgZ3o3v2IxpVDJ+kvK+bRO',
  # Best practice for higher availability in librdkafka clients prior to 1.7
  'session.timeout.ms': str(45000),
  'group.id': 'top-selling-products-group',
  'auto.offset.reset': 'earliest',
  'taskmanager.rpc.port': '6122-6130'
}



TOPIC = "orders"


# Define the Kafka consumer to read orders from the "orders" topic
def create_kafka_consumer():
    kafka_consumer = FlinkKafkaConsumer(
        topics='orders',
        deserialization_schema=SimpleStringSchema(),
        properties=CONFIG
    )
    return kafka_consumer

# Define the Kafka producer to write top-selling products to the "top-selling-products" topic
def create_kafka_producer():

    kafka_producer = FlinkKafkaProducer(
        topic='top-selling-products',
        serialization_schema=SimpleStringSchema(),
        producer_config=CONFIG
    )
    return kafka_producer

# Map function to convert order JSON string to (product, quantity) tuple
def map_order_to_product(order_str):
    order = json.loads(order_str)
    product = order['product']
    quantity = order['quantity']
    return product, quantity

# Main Flink job definition
def top_selling_products():
    # Set up the execution environment
    env = StreamExecutionEnvironment.get_execution_environment(CONFIG)

    # Add Kafka consumer as a source to the data stream
    kafka_consumer = create_kafka_consumer()
    orders_stream = env.add_source(kafka_consumer).name("Kafka Orders Source")

    # Map the input data stream to extract product and quantity information
    product_sales_stream = orders_stream.map(
        lambda order: map_order_to_product(order),
        output_type=Types.TUPLE([Types.STRING(), Types.INT()])
    )

    # Aggregate sales by product within a 5-minute tumbling window
    top_selling_products_stream = product_sales_stream \
        .key_by(lambda order: order[0]) \
        .window(TumblingEventTimeWindows.of(Time.minutes(5))) \
        .sum(1)

    # Convert the result to string for Kafka producer
    top_selling_products_string_stream = top_selling_products_stream.map(
        lambda product_tuple: f"{product_tuple[0]}:{product_tuple[1]}",
        output_type=Types.STRING()
    )

    # Add Kafka producer to send the top-selling products to the output topic
    kafka_producer = create_kafka_producer()
    top_selling_products_string_stream.add_sink(kafka_producer).name("Kafka Top Selling Products Sink")

    # Execute the job
    env.execute("Top Selling Products Job")
    print('finished')

# Run the Flink job
if __name__ == '__main__':
    top_selling_products()
