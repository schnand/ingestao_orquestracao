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

# Define queue
#queue_name = 'work_queues_durable' #não é possível redefinir uma fila existente

# Define exchange name
exchange_name = 'logs'

# Declare exchange
channel.exchange_declare(
    exchange=exchange_name,
    exchange_type='fanout'
)

# Create queue
#channel.queue_declare(
#    queue=queue_name,
#    durable=True
#)

# Create and publish messages
for i in range (100000):

    # Assemble message
    time_stamp = dt.datetime.strftime(dt.datetime.now(), format='%Y-%m-%d %H:%M:%S.%f')
    
    # NOVA TAREFA
    message = f'{time_stamp} {i:6} {"."*random.randint(1,10)}'

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