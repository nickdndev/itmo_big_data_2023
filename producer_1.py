import random
from json import dumps
from time import sleep

from kafka import KafkaProducer
from kafka import errors


def write_data(producer):
    data_cnt = 20000
    topic = "itmo2023"

    for i in range(data_cnt):
        device_id = random.randint(1, 10)
        temperature = random.uniform(60, 110) + 273
        execution_time = i * 5
        cur_data = {"device_id": device_id, "temperature": temperature, "execution_time": execution_time}
        producer.send(topic,
                      key=dumps(device_id).encode('utf-8'),
                      value=cur_data)
        print(f"Data was sent to topic [{topic}]: {cur_data}")
        sleep(1)


def create_producer():
    print("Connecting to Kafka brokers")
    for i in range(0, 6):
        try:
            producer = KafkaProducer(bootstrap_servers=['localhost:29092'],
                                     value_serializer=lambda x: dumps(x).encode('utf-8'),
                                     acks=1
                                     )
            print("Connected to Kafka")
            return producer
        except errors.NoBrokersAvailable:
            print("Waiting for brokers to become available")
            sleep(5)

    raise RuntimeError("Failed to connect to brokers within 60 seconds")


if __name__ == '__main__':
    producer = create_producer()
    write_data(producer)
