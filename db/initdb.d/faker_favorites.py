from faker import Faker
import random

faker = Faker()

for num in range(1, 10):
  print(
      f'INSERT INTO favorites (user_id, tweet_id, create_at) VALUES ({random.randint(1,10)}, {num}, NOW());')
