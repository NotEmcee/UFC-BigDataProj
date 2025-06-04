from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'ufc-events',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v)
)

print("Consuming UFC fighters from Kafka...")

for message in consumer:
    fighter = message.value
    print(f"Received fighter: {fighter.get('FirstName', '')} {fighter.get('LastName', '')}")
