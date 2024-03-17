
import pika
from models import Contact
import json
import faker
import connect
import mongoengine


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

# Створення фейкових контактів та збереження їх у базу даних MongoDB
fake = faker.Faker()
for _ in range(10):
    contact = Contact(
        fullname=fake.name(),
        email=fake.email()
    )
    contact.save()

    # Відправка повідомлення до черги RabbitMQ
    channel.basic_publish(exchange='', routing_key='task_queue', body=str(contact.id))

print("Contacts sent to RabbitMQ")

# Закриття з'єднання з RabbitMQ
connection.close()
