from kafka import KafkaProducer

def send_hello_world(bootstrap_servers, topic_name):
    """
    Sends the message "HELLO WORLD" to the specified Kafka topic.

    Args:
        bootstrap_servers (str): Comma-separated list of Kafka broker addresses (e.g., 'localhost:9092').
        topic_name (str): The name of the Kafka topic to send the message to (e.g., 'ABC').
    """
    try:
        producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
        message = "HELLO WORLD".encode('utf-8')
        producer.send(topic_name, message)
        producer.flush()  # Wait for all messages to be sent
        print(f"Message 'HELLO WORLD' sent successfully to topic '{topic_name}'")
    except Exception as e:
        print(f"Error sending message: {e}")
    finally:
        if 'producer' in locals() and producer is not None:
            producer.close()

if __name__ == "__main__":
    kafka_brokers = 'localhost:9092'  # Replace with your Kafka broker address if different
    topic = 'ABC'
    send_hello_world(kafka_brokers, topic)