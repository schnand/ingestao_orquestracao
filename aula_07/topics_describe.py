from kafka.admin import KafkaAdminClient

# Cria uma instância do KafkaAdminClient
admin_client = KafkaAdminClient(
    bootstrap_servers='localhost:9092',
)

# Define o nome do tópico a ser descrito
topic_name = admin_client.list_topics()

# Descreve o tópico
topic_description = admin_client.describe_topics(topic_name)

print(topic_description)

# Exibe as informações do tópico
for topic in topic_description: #[0].items():
    print(f'Tópico: {topic["topic"]}')
    print(f'Número de partições: {len(topic["partitions"])}')
    print(f'Replicas: {topic["partitions"][0]["replicas"]}')
    print(f'Líder: {topic["partitions"][0]["leader"]}')