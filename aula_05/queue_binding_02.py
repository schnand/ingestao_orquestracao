import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Define o padrão de roteamento
pattern = 'eventos_importantes'

# Faz o binding entre a fila e o padrão de roteamento
channel.queue_bind(exchange='exchange_direct', 
                   queue='participacao_obrigatoria_it', 
                   routing_key=pattern    
            )

channel.queue_bind(exchange='exchange_direct', 
                   queue='participacao_obrigatoria_sales', 
                   routing_key=pattern    
            )

channel.queue_bind(exchange='exchange_direct', 
                   queue='participacao_obrigatoria_mkt', 
                   routing_key=pattern    
            )


channel.queue_bind(exchange='exchange_direct', 
                   queue='participacao_obrigatoria_rh', 
                   routing_key=pattern    
            )
            
connection.close()
