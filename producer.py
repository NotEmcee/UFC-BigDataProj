import requests
from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9094',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    retries=5
)


while True:
    print("Fetching UFC fighters...")
    try:
        response = requests.get("https://api.sportsdata.io/v3/mma/scores/json/FightersBasic?key=a4a6485d442142388c4362cdcd100929")
        response.raise_for_status()  # lance une exception si code != 200
        fights = response.json()
        for fight in fights:
            future = producer.send('ufc-events', fight)
            future.get(timeout=10)  # attendre la confirmation d'envoi
            first = fight.get("FirstName") or ""
            last = fight.get("LastName") or ""
            print("Sent fighter:", (first + " " + last).strip())
    except Exception as e:
        print("Error:", e)
    time.sleep(60)
