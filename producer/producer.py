import time
import random
from kafka import KafkaProducer
import redis
import json

# Conexión a Kafka
producer = KafkaProducer(bootstrap_servers='kafka:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Conexión a Redis
r = redis.Redis(host='redis', port=6379, db=0)

def generate_price_event():
    while True:
        ticket_id = random.randint(1, 100)
        price = round(random.uniform(10, 100), 2)
        event = {'ticket_id': ticket_id, 'price': price}

        # Publicar evento en Kafka
        producer.send('ticket_prices', event)
        # producer.flush()

        # Guardar precio en Redis
        r.set(f'ticket:{ticket_id}', price)

        print(f'Published: {event}')
        time.sleep(2)

if __name__ == "__main__":
    generate_price_event()
