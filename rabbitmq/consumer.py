import pika

from config import RABBITMQ_HOST, RABBITMQ_QUEUE


def consume_messages(process_message_callback):
    credentials = pika.PlainCredentials("guest", "guest")
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=RABBITMQ_HOST, port=5672, credentials=credentials
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
