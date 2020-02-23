from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop

class MainHandler(RequestHandler):
  async def get(self):
    self.write({'message': 'hello world'})


def make_app():
  urls = [
      ("/", MainHandler)
  ]
  return Application(urls, debug=True)

if __name__ == "__main__":
  app = make_app()
  app.listen(8080)
  IOLoop.instance().start()
