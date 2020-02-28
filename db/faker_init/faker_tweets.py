from faker import Faker
import random

faker = Faker()

for num in range(1, 10):
  print(
      f'INSERT INTO tweets (tweet_txt, user_id, is_delete, create_at, update_at) VALUES (\'{faker.text()}\', {num}, {bool(random.getrandbits(1))}, NOW(), NOW());')


