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


categories = ['ERRORS']
priorities = ['ALTA', 'MEDIA', 'BAIXA']
statuses = ['ABERTA', 'ENCERRADA']
department = 'IT'

# Create a message 
for i in range (15):

    # Assemble message
    category = random.choice(categories)
    priority = random.choice(priorities)
    status = random.choice(statuses)

    time_stamp = dt.datetime.strftime(dt.datetime.now(), format='%Y-%m-%d %H:%M:%S.%f')
    message = f'{time_stamp} {i:6} Mensagem criada por {department} com prioridade {priority} para informar sobre {category} com status {status}.'


## REGRAS DE ENVIO
    exchange_name1 = 'exchange_fanout'
    exchange_name2 = 'exchange_topic'

## 1. Todos os logs são publicados no modo *fanout*.

    # Publish message
    channel.basic_publish(
        exchange=exchange_name1,
        routing_key='',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))

    

## 2. Todos erros de alta prioridade em aberto são publicados no modo *topic*, rota *department.category.priority.status*.

    if category == 'ERRORS' and priority == 'ALTA' and status == 'ABERTA':

        routing_key_ = f'{department.lower()}.{category.lower()}.{priority.lower()}.{status.lower()}'
        
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