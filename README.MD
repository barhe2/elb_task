# Home Assignment - Message Queuing and System Monitoring

This README provides instructions on how to set up and run the Python scripts for the message queuing system (using Kafka) and the CPU usage monitoring service.

## 1. Message Queuing System (Kafka)git 

This section describes how to set up Kafka (using Docker Compose) and run the publisher and consumer scripts.

### Prerequisites

- **Docker:** You need to have Docker installed on your system. You can find installation instructions for your operating system here: [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)
- **Docker Compose:** Docker Compose is usually installed along with Docker Desktop. If you installed Docker Engine separately, you might need to install Docker Compose separately. Instructions can be found here: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)
- **Python 3:** Python 3 should be installed on your system.
- **pip:** pip is the package installer for Python and should be installed with Python.

### Running the Publisher Script

1.  **Navigate to the directory containing `producer.py`** (provided in the submission).

2.  **Install the `kafka-python` library:** If you haven't already, install the required library using pip:

    pip install -r requirements.txt

    (Ensure that the `requirements.txt` file in the same directory).

3.  **Run the publisher script:** Execute the script using the Python interpreter:

    ```bash
    python producer.py
    ```

    This script will connect to the Kafka broker running on `localhost:9092` and send "HELLO WORLD" to the "ABC" topic.

### Running the Consumer Script

1.  **Navigate to the directory containing `consumer.py`** (provided in the submission).

2.  **Ensure the `kafka-python` library is installed** (as described in the publisher section).

3.  **Run the consumer script:** Execute the script using the Python interpreter:

    python3 consumer.py

    This script will connect to the Kafka broker and start listening for messages on the "ABC" topic. Any messages sent by the publisher will be printed to the console.