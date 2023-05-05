from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(
    bootstrap_servers=["localhost:9092"],
)

topic = NewTopic(
    name="my_topic",
    num_partitions=1,
    replication_factor=1
)

admin_client.create_topics([topic])