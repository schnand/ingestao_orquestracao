import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Define o padrão de roteamento
patternies = ['eventos_importantes','orcamentos','ordens']

# Faz o binding entre a fila e o padrão de roteamento
channel.queue_bind(exchange='exchange_fanout', 
                   queue='logs', 
                   routing_key=''    
            )

for pattern in patternies:
        channel.queue_bind(
            exchange='exchange_direct',
            queue='logs',
            routing_key=pattern
        )

channel.queue_bind(exchange='exchange_topic', 
                   queue='logs', 
                   routing_key='#'    
            )                                    
connection.close()
