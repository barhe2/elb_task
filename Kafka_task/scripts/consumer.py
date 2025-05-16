from kafka import KafkaConsumer

kafka_brokers = 'localhost:9092'  # Kafka broker address here is for local testing only
topic = 'ABC'

def consume_send_message(bootstrap_servers, topic_name):
    # Consumes messages from the specified Kafka topic and prints them at the terminal.

    try:
        consumer = KafkaConsumer(
            topic_name,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset='earliest',  # Start consuming the topic
            enable_auto_commit=True,
            group_id='my-consumer-group',
            value_deserializer=lambda x: x.decode('utf-8')
        )

        print(f"Consumer listening for messages on topic '{topic_name}'...")
        for message in consumer:
            print(f"Received message: {message.value}")

    except Exception as e:
        print(f"Error consuming messages: {e}")
    finally:
        if 'consumer' in locals() and consumer is not None:
            consumer.close()

if __name__ == "__main__":
    consume_send_message(kafka_brokers, topic)