import pika
import sys
import os
import time


def main():
    # Create a connection to the RabbitMQ server running on the local machine
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    #queue_name = 'work_queues_durable' #não é possível redefinir uma fila existente


    # Declare a queue to consume messages from
    result = channel.queue_declare(queue='', exclusive=True)

    queue_name = result.method.queue

     # Define exchange and queue name s
    exchange_name = 'direct_logs'
    queue_name = result.method.queue

    # Declare exchange
    channel.exchange_declare(
        exchange=exchange_name,
        exchange_type='direct'
    )

    # Declare queue bindings
    severities = ['error', 'warning', 'info']
    # severities = ['error'] # for errors only channel
    
    for severity in severities:
        channel.queue_bind(
            exchange=exchange_name,
            queue=queue_name,
            routing_key=severity
        )

    #channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

    #binding_keys = sys.argv[1:]

    # Define a callback function to handle incoming messages
    def callback(ch, method, properties, body):
        message = f" [x] Received {method.routing_key}: {body}"
        print(message)
       
        ch.basic_ack(delivery_tag=method.delivery_tag)        
        print(" [x] Done")


    # Set up a consumer to receive messages from the queue and pass them to the callback function
    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback,
        # auto_ack=True
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