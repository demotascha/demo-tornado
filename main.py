from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json

tweets = []

class MainHandler(RequestHandler):
  async def get(self):
    self.write({'message': 'hello world'})

class UserTweets(RequestHandler):
  def get(self):
    self.write({'tweets': tweets})

class UserTweet(RequestHandler):
  def post(self, _):
    tweets.append(json.loads(self.request.body))
    self.write({'message': 'new tweet added'})

  def delete(self, id):
    global tweets
    new_items = [tweet for tweet in tweets if tweet['id'] is not int(id)]
    tweets = new_items
    self.write({'message': 'Tweet with id %s was deleted' % id})

def make_app():
  urls = [
    ("/", UserTweets),
    (r"/tweet/([^/]+)?", UserTweet)
  ]
  return Application(urls, debug=True)

if __name__ == "__main__":
  app = make_app()
  app.listen(8080)
  IOLoop.instance().start()
