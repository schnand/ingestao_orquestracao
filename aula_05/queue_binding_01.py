import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Define o padrão de roteamento
pattern = 'it.*.alta.*'

# Faz o binding entre a fila e o padrão de roteamento
channel.queue_bind(exchange='exchange_topic', 
                   queue='informacoes_criticas', 
                   routing_key=pattern    
            )

connection.close()
