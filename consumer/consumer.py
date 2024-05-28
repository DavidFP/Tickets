from kafka import KafkaConsumer
import redis
import json
import time

# Conexión a Kafka
consumer = KafkaConsumer('ticket_prices',
                         bootstrap_servers='kafka:9092',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# Conexión a Redis
r = redis.Redis(host='redis', port=6379, db=0)

def consume_price_event():
    while True:
        for message in consumer:
            event = message.value
            ticket_id = event['ticket_id']
            price = event['price']
            print(f'TicketId: {ticket_id} Price: {price}')
            # Actualizar precio en Redis
            r.set(f'ticket:{ticket_id}', price)
            print(f'Updated in Redis: {event}')
    
if __name__ == "__main__":
    consume_price_event()
