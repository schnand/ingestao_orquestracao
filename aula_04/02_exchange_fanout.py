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
exchange_name = 'fanout'

# Declare exchange
channel.exchange_declare(
    exchange=exchange_name,
    exchange_type='fanout'
)