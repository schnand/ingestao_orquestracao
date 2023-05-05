import pika
import sys
import os
import time


def main():
    # Create a connection to the RabbitMQ server running on the local machine
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    queue_name = 'work_queues_durable'

    # Declare a queue to consume messages from
    channel.queue_declare(
    queue=queue_name,
    durable=True
)

    # Define a callback function to handle incoming messages
    # Define a callback function to handle incoming messages
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

        # Simulate work being done on the message by sleeping for an amount of time
        time.sleep(body.count(b'.'))
        print(" [x] Done")

        ch.basic_ack(delivery_tag = method.delivery_tag)
    channel.basic_qos(prefetch_count=1)


    # Set up a consumer to receive messages from the queue and pass them to the callback function
    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback,
        #auto_ack=True
    )

    # Start consuming messages from the queue
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')

        # Attempt to exit gracefully
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)