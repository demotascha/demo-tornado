import json
from psycopg2 import connect

table_name = "tweets"

# declare connection instance
conn = connect(
    dbname="postgres",
    user="postgres",
    host="db",
    password="mysecretpassword"
)

# declare a cursor object from the connection
cursor = conn.cursor()

tweets = []
replies = []
favorites = []
# execute an SQL statement using the psycopg2 cursor object
cursor.execute(
    f"SELECT tweet_id, tweet_txt FROM {table_name};")
for i, record in enumerate(cursor):
    tweet = {}
    tweet["tweet_id"] = record[0]
    tweet["tweet_txt"] = record[1]
    tweets.append(tweet)

# replies
cursor.execute(
    f"SELECT user_id, tweet_id, reply_text, create_at FROM reply;")
for i, record in enumerate(cursor):
    reply = {}
    reply["user_id"] = record[0]
    reply["tweet_id"] = record[1]
    reply["reply_text"] = record[2]
    replies.append(reply)

# favorites
cursor.execute(
    f"SELECT user_id, tweet_id, create_at FROM favorites;")
for i, record in enumerate(cursor):
    favorite = {}
    favorite["user_id"] = record[0]
    favorite["tweet_id"] = record[1]
    favorites.append(favorite)

print({'tweets': json.dumps(tweets), 'reply': json.dumps(
    replies), 'favorites': json.dumps(favorites)})

# close the cursor object to avoid memory leaks
cursor.close()

# close the connection as well
conn.close()
