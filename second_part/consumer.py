
import pika
from models import Contact
import connect

def callback(ch, method, properties, body):
    contact_id = body.decode('utf-8')

    # Отримання контакту з бази даних MongoDB
    contact = Contact.objects(id=contact_id).first()

    if contact:
        # Імітація надсилання електронної пошти (можна замінити на реальне надсилання пошти)
        print(f"Sending email to {contact.email}")

        # Оновлення логічного поля is_sent в базі даних
        contact.is_sent = True
        contact.save()

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
channel.basic_consume(queue='task_queue', on_message_callback=callback, auto_ack=True)

print("Consumer started. Waiting for messages...")

# Початок отримання повідомлень
channel.start_consuming()
