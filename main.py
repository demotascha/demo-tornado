from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json

reply = []
tweets = []


def get_json_arg(req_body, fields):
  """
  Gets argument from JSON
  """
  results = {}
  for i in fields:
    results[i] = json.loads(req_body).get(i)
  return results

def get_filtered(id):
  """
  Filters list to pick one tweet
  """
  result = [tweet for tweet in tweets if tweet['user_id'] == int(id)]
  return result

class MainHandler(RequestHandler):
  async def get(self):
    self.write({'message': 'hello world'})

class UserTweets(RequestHandler):
  def get(self):
    self.write({'tweets': tweets, 'reply': reply})

class UserTweet(RequestHandler):
  def post(self, _):
    tweets.append(json.loads(self.request.body))
    self.write({'message': 'new tweet added'})

  def put(self, id):
    picked_item = get_filtered(id)
    if picked_item:
      tweets.remove(picked_item[0])
      tweet = get_json_arg(self.request.body, ['text'])
      tweet['user_id'] = int(id)
      tweets.append(tweet)
      self.write({'message': 'Tweet with id %s was updated.' % id})

  def delete(self, id):
    global tweets
    new_tweets = [tweet for tweet in tweets if tweet['id'] is not int(id)]
    tweets = new_tweets
    self.write({'message': 'Tweet with id %s was deleted' % id})

class UserReply(RequestHandler):
  def post(self, _):
    reply.append(json.loads(self.request.body))
    self.write({'message': 'add tweet replied'})

def make_app():
  urls = [
    ("/", UserTweets),
    (r"/tweet/([^/]+)?", UserTweet),
    (r"/tweet/reply/([^/]+)?", UserReply)
  ]
  return Application(urls, debug=True)

if __name__ == "__main__":
  app = make_app()
  app.listen(8080)
  IOLoop.instance().start()
