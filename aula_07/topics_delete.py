from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(
    bootstrap_servers=["localhost:9092"]
)

topics_to_delete = ['my_topic', 'teste1', '__consumer_offsets']
delete_result =  admin_client.delete_topics(topics_to_delete)

print(delete_result)