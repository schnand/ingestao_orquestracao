import pika
import sys
import os
import time
import random
import smtplib
from email.mime.text import MIMEText

def main():
    # Create a connection to the RabbitMQ server running on the local machine
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()


    # Declare a queue to consume messages from
    result = channel.queue_declare(
        queue='', 
        exclusive=True
    )

    # Define exchange and queue name s
    exchange_name = 'exchange_fanout'
    queue_name = result.method.queue

    """ # Declare exchange
    channel.exchange_declare(
        exchange=exchange_name,
        exchange_type='fanout'
    ) """

    # Declare queue bindings
    channel.queue_bind(
        exchange=exchange_name,
        queue=queue_name
    )
 
    # Define a callback function to handle incoming messages
    def callback(ch, method, properties, body):
        
        print(f" [x] Received {body}")
        print(f"{method.routing_key}")
        #time.sleep(random.randint(1,20))
        ch.basic_ack(delivery_tag=method.delivery_tag)

        # define o conteúdo do email a ser enviado
        """ msg = MIMEText(f" [x] Received {body}")
        msg['Subject'] = 'Nova mensagem do RabbitMQ'
        msg['From'] = 'seu-email@provedor.com'
        msg['To'] = 'destinatario@provedor.com'         """

        # envia o email utilizando um servidor SMTP
        """ with smtplib.SMTP('smtp.provedor.com', 587) as smtp:
            smtp.login('seu-email@provedor.com', 'senha')
            smtp.sendmail('seu-email@provedor.com', ['destinatario@provedor.com'], msg.as_string()) """

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