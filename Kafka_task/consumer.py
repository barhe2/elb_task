from kafka import KafkaConsumer

def consume_hello_world(bootstrap_servers, topic_name):
    #Consumes messages from the specified Kafka topic and prints them at terminal.

    try:
        consumer = KafkaConsumer(
            topic_name,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset='earliest',  # Start consuming from the beginning of the topic
            enable_auto_commit=True,
            group_id='my-consumer-group',  # Assign a consumer group ID
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
    kafka_brokers = 'localhost:9092'  # Replace with your Kafka broker address if different
    topic = 'ABC'
    consume_hello_world(kafka_brokers, topic)