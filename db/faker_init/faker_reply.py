from faker import Faker
import random

faker = Faker()

for num in range(1, 10):
  print(
      f'INSERT INTO reply (user_id, tweet_id, reply_text, create_at) VALUES ({random.randint(1,10)}, {num}, \'{faker.text()}\', NOW());')
