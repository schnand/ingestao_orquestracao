# Importa a classe KafkaConsumer da biblioteca kafka-python
from kafka import KafkaConsumer

# Cria uma instância de um consumidor Kafka e configura o endereço do servidor de bootstrap e o nome do tópico a ser consumido
consumer = KafkaConsumer(
    'my_topic', 
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset = 'latest'
)

# Itera sobre as mensagens recebidas pelo consumidor
for message in consumer:
    # Decodifica a mensagem e a imprime no console
    print(message.value.decode('utf-8'))