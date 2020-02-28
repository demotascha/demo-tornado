from faker import Faker
import random

faker = Faker()

for num in range(1, 10):
  print(
      f'INSERT INTO connections (follower_id, followee_id, create_at) VALUES ({num}, {random.randint(1,9)}, NOW());')
