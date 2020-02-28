from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from dotenv import load_dotenv
from psycopg2 import connect

import json
import os

load_dotenv()

conn = connect(
  host = os.getenv("HOST"),
  dbname = os.getenv("POSTGRES_DB"),
  user = os.getenv("POSTGRES_USER"),
  password = os.getenv("POSTGRES_PASSWORD")
)

# declare a cursor object from the connection
cursor = conn.cursor()

def get_json_arg(req_body, fields):
  """
  Gets argument from JSON
  """
  results = {}
  for i in fields:
    results[i] = json.loads(req_body).get(i)
  return results

# def get_filtered(id):
#   """
#   Filters list to pick one tweet
#   """
#   result = [tweet for tweet in tweets if tweet['user_id'] == int(id)]
#   return result

class MainHandler(RequestHandler):
  async def get(self):
    self.write({'message': 'hello world'})

class UserTweets(RequestHandler):
  async def get(self):
    favorites = []
    replies = []
    tweets = []
    # tweet
    cursor.execute(
      f"SELECT tweet_id, tweet_txt FROM tweets;")
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
    self.write({'tweets': tweets, 'reply': replies, 'favorites': favorites})

class UserTweet(RequestHandler):
  async def post(self, _):
    # tweets.append(json.loads(self.request.body))
    self.write({'message': 'new tweet added'})

  async def put(self, id):
    # picked_item = get_filtered(id)
    # if picked_item:
    #   tweets.remove(picked_item[0])
    #   tweet = get_json_arg(self.request.body, ['text'])
    #   tweet['user_id'] = int(id)
    #   tweets.append(tweet)
      self.write({'message': 'Tweet with id %s was updated.' % id})

  async def delete(self, id):
    self.write({'message': 'Tweet with id %s was deleted' % id})

class UserReply(RequestHandler):
  async def post(self, _):
    self.write({'message': 'add tweet replied'})

class UserLike(RequestHandler):
  async def post(self, _):
    self.write({'message': 'add tweet liked'})

def make_app():
  urls = [
    ("/", UserTweets),
    (r"/tweet/([^/]+)?", UserTweet),
    (r"/tweet/like/([^/]+)?", UserLike),
    (r"/tweet/reply/([^/]+)?", UserReply)
  ]
  return Application(urls, debug=True)

if __name__ == "__main__":
  app = make_app()
  app.listen(8080)
  IOLoop.instance().start()
