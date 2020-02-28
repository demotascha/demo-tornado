from faker import Faker

faker = Faker()

for num in range(1, 10):
  print(
      f'INSERT INTO users (name, followers_count, create_at, update_at) VALUES (\'{faker.name()}\', 0, NOW(), NOW());')
