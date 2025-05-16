from kafka import KafkaProducer
import time

kafka_brokers = 'localhost:9092'  # Kafka broker address here is for local testing only
topic = 'ABC'

def send_message(bootstrap_servers, topic_name):
    try:
        producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
        message = "Hello World".encode('utf-8')
        for i in range(10):
            producer.send(topic_name, message)
            producer.flush()
            time.sleep(0.1)  # Add a small delay
        print(f"Message 'Hello World' sent successfully to topic '{topic_name}'")
    except Exception as e:
        print(f"Error sending message: {e}")
    finally:
        if 'producer' in locals() and producer is not None:
            producer.close()

if __name__ == "__main__":
    send_message(kafka_brokers, topic)