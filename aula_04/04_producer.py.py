from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
topic = 'my_topic'
# topic = 'kontext-events'

for i in range(1):
    msg = "Mensagem {}".format(i)
    producer.send(topic, msg.encode('utf-8'))

producer.flush()