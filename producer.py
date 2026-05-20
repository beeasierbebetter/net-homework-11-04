import pika

from settings import URI

# params = pika.ConnectionParameters('localhost')
params = pika.URLParameters(URI)
conn = pika.BlockingConnection(params)
channel = conn.channel()

channel.queue_declare(
    queue="hello",
    durable=True
)

if __name__ == "__main__":

    count = 0

    while True:
        channel.basic_publish(
            exchange="",
            routing_key="hello",
            body=f"Hello, SYSDB-54! - {count}",
        )
        count += 1
 
