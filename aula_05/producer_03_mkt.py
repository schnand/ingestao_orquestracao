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


categories = ['EVENTO', 'PROMOCAO']
priorities = ['ALTA', 'MEDIA', 'BAIXA']
# statuses = ['ABERTA', 'ENCERRADA']
department = 'MKT'

# Create a message 
for i in range (15):

    # Assemble message
    category = random.choice(categories)
    priority = random.choice(priorities)
    # status = random.choice(statuses)

    time_stamp = dt.datetime.strftime(dt.datetime.now(), format='%Y-%m-%d %H:%M:%S.%f')
    message = f'{time_stamp} {i:6} Mensagem criada por {department} com prioridade {priority} para informar sobre {category}.'


## REGRAS DE ENVIO
    exchange_name1 = 'exchange_direct'
    exchange_name2 = 'exchange_topic'

## 1. Eventos importantes (prioridade alta) são publicados no modo *direct*, rota *eventos_importantes*.

    if priority == 'ALTA':

        routing_key_ = 'eventos_importantes'
        
        channel.basic_publish(
            exchange=exchange_name1, 
            routing_key=routing_key_, 
            body=message,
            properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    )
            )

## 2. Todas as promoções são publicadas no modo *topic*, rota *department.category.priority*.

    if category == 'PROMOCAO':

        routing_key_ = f'{department.lower()}.{category.lower()}.{priority.lower()}'
        
        channel.basic_publish(
            exchange=exchange_name2, 
            routing_key=routing_key_, 
            body=message,
            properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    )
            )


    print(f" [x] Sent {message}")
    time.sleep(random.randint(0,3))



# Close the connection
connection.close()