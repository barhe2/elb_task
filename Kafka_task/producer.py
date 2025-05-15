from kafka import KafkaProducer

def send_hello_world(bootstrap_servers, topic_name):
    #Sends the message "HELLO WORLD" to the specified Kafka topic.

    try:
        producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
        message = "Hello World".encode('utf-8')
        for i in range(10):
            producer.send(topic_name, message)
            producer.flush()  # Wait for all messages to be sent
        print(f"Message 'Hello World' sent successfully to topic '{topic_name}'")
    except Exception as e:
        print(f"Error sending message: {e}")
    finally:
        if 'producer' in locals() and producer is not None:
            producer.close()

if __name__ == "__main__":
    kafka_brokers = 'localhost:9092'  # Replace with your Kafka broker address if different
    topic = 'ABC'
    send_hello_world(kafka_brokers, topic)