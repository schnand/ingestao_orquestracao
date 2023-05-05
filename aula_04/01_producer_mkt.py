import pika
import datetime as dt
import time
import random

# Establish a connection with RabbitMQ server
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

# Create a channel
channel = connection.channel()

exchange_list = ['fanout','direct','topics']
routing_list = ['promo','info']    

for i in range (1000):

    # Assemble message
    time_stamp = dt.datetime.strftime(dt.datetime.now(), format='%Y-%m-%d %H:%M:%S.%f')
    
    # NOVA TAREFA
    message = f'{time_stamp} {i:6} {"."*random.randint(1,10)}'

    for exchange_name in exchange_list: 

        if exchange_name == 'fanout':
            
            # Publish message
            channel.basic_publish(
            exchange=ex change_name,
            routing_key='',
            body=message
        )
            
        elif exchange_name == 'direct':
             
            if len(priority) <= 2:
                routing_key = 'error'
            elif len(priority) <= 4:
                routing_key = 'warning'
            else:
                routing_key = 'info'

            # Publish message
            channel.basic_publish(
            exchange=exchange_name,
            routing_key='',
            body=message
        )

    time.sleep(1)

    print(f" [x] Sent {message}")

# Close the connection
connection.close()