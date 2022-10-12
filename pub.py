import redis

# initializing the redis instance
r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    decode_responses=True 
)
while True:
    message = input("Enter the message you want to send to subscribers: ")

    r.publish("publisher", message)