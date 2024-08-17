from flask_app.server import create_app
from flask_app.__share.config import enviroment

enviroment.load()
app = create_app()

if __name__ == '__main__':
  app.run()