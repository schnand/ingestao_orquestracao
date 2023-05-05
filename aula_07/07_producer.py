from kafka import KafkaProducer   # Importa a classe KafkaProducer da biblioteca kafka-python
import datetime as dt   # Importa a biblioteca datetime para trabalhar com datas e horas
import time   # Importa a biblioteca time para adicionar atrasos ao envio das mensagens

# Cria uma instância de um produtor Kafka e configura o endereço do servidor de bootstrap
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])   

# Define o nome do tópico para enviar as mensagens
topic_ = 'my_topic'   

# Cria uma mensagem
for i in range (20):
    # Captura a hora atual e converte em uma string formatada
    time_stamp = dt.datetime.strftime(dt.datetime.now(), format='%Y-%m-%d %H:%M:%S.%f')   
    # Monta uma mensagem com um carimbo de data/hora e um número de sequência
    message_ = f'{time_stamp} {i:6} Essa mensagem é enviada por KafkaProducer.'   


    # Imprime uma confirmação de mensagem enviada,
    print(f'Sent: {message_}')
    # Envia a mensagem ao tópico especificado pelo produtor
    producer.send(
        topic=topic_, 
        value=message_.encode('utf-8')
    )   

    time.sleep(1)

# Força o envio de todas as mensagens pendentes antes de fechar o produtor.
producer.flush()   

# Fecha a conexão com o produtor
producer.close()