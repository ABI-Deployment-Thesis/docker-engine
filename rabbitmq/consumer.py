import time

import pika

from config import RABBITMQ_HOST, RABBITMQ_QUEUE


def consume_messages(process_message_callback, retries=12, delay=5):
    for i in range(retries):
        try:
            # Increased heartbeat interval, otherwise if the build takes too long, the RabbitMQ connection will be broken
            credentials = pika.PlainCredentials("guest", "guest")
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=RABBITMQ_HOST,
                    port=5672,
                    credentials=credentials,
                    heartbeat=60 * 60,  # 1 hour
                )
            )
            channel = connection.channel()
            channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
            channel.basic_qos(prefetch_count=1)
            channel.basic_consume(
                queue=RABBITMQ_QUEUE, on_message_callback=process_message_callback
            )
            print("Waiting for messages. To exit press CTRL+C")
            channel.start_consuming()
            break
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Attempt {i+1} failed: {e}")
            time.sleep(delay)
    else:
        print(f"Failed to connect to RabbitMQ after {retries} attempts")
