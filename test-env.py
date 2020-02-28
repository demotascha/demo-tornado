import os
from dotenv import load_dotenv
load_dotenv()

print(os.getenv("HOST"))
print(os.getenv("POSTGRES_DB"))
print(os.getenv("POSTGRES_USER"))
print(os.getenv("POSTGRES_PASSWORD"))
