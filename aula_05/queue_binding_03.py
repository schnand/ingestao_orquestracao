import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Define o padrão de roteamento
pattern1 = 'orcamentos'
pattern2 = 'ordens'

# Faz o binding entre a fila e o padrão de roteamento
channel.queue_bind(exchange='exchange_direct', 
                   queue='compras', 
                   routing_key=pattern1    
            )

channel.queue_bind(exchange='exchange_direct', 
                   queue='compras', 
                   routing_key=pattern2    
            )
            
connection.close()
