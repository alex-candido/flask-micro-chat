from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__name__), '.env')

def load():
  load_dotenv(dotenv_path)