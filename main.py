from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop

tweets = []

class MainHandler(RequestHandler):
  async def get(self):
    self.write({'message': 'hello world'})

class UserTweets(RequestHandler):
  def get(self):
    self.write({'tweets': tweets})

def make_app():
  urls = [
    ("/", UserTweets)
  ]
  return Application(urls, debug=True)

if __name__ == "__main__":
  app = make_app()
  app.listen(8080)
  IOLoop.instance().start()
