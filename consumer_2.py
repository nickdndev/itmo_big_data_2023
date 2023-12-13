from kafka import KafkaConsumer


@backoff(tries=10,sleep=60)
def message_handler(value)->None:
    print(value)


def create_consumer():
    print("Connecting to Kafka brokers")
    consumer = KafkaConsumer("itmo2023",
                             group_id='itmo_group1',
                             bootstrap_servers='localhost:29092',
                             auto_offset_reset='earliest',
                             enable_auto_commit=True)

    for message in consumer:
        # send to http get (rest api) to get response
        # save to db message (kafka) + external
        message_handler(message)
        print(message)




if __name__ == '__main__':
    create_consumer()
