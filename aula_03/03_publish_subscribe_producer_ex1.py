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

# Define exchange name
exchange_name = 'direct_logs'

# Declare exchange
channel.exchange_declare(
    exchange=exchange_name,
    exchange_type='direct'
)

# Define routing keys
routing_keys = ['error', 'warning', 'info']

# Create and publish messages
for i in range (1000):

    # Assemble message
    time_stamp = dt.datetime.strftime(dt.datetime.now(), format='%Y-%m-%d %H:%M:%S.%f')

    priority = '.' * random.randint(1, 10)
    
    # NOVA TAREFA
    message = f'{time_stamp} {i:6} {priority}'

   # Choose routing key based on message priority
    if len(priority) <= 2:
        routing_key = 'error'
    elif len(priority) <= 4:
        routing_key = 'warning'
    else:
        routing_key = 'info'

    # Publish message
    channel.basic_publish(
        exchange=exchange_name,
        routing_key=routing_key,
        body=message
    )
    time.sleep(1)

    print(f" [x] Sent {message}")

# Close the connection
connection.close()