import pika
import sys
import os
import time
import random


def main():
    # Create a connection to the RabbitMQ server running on the local machine
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()


    # Declare a queue to consume messages from
    result = channel.queue_declare(
        queue='', 
        exclusive=True
    )

    queue_name = result.method.queue

    patternies = ['orcamentos', 'ordens']
    
    # Declare queue bindings

    channel.queue_bind(
        exchange='exchange_fanout',
        queue=queue_name
    )

    channel.queue_bind(
        exchange='exchange_topic',
        queue=queue_name,
        routing_key='rh.movimentacao.*'
    )

    for pattern in patternies:
        channel.queue_bind(
            exchange='exchange_direct',
            queue=queue_name,
            routing_key=pattern
        )
 
    # Define a callback function to handle incoming messages
    def callback(ch, method, properties, body):
        
        print(f" [x] Received {body}")
        print(f"{method.routing_key}")
        #time.sleep(random.randint(1,20))
        ch.basic_ack(delivery_tag=method.delivery_tag)

        print('[X] Done.')

    channel.basic_qos(prefetch_count=1)
    
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