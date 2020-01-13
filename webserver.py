from flask import Flask
from threading import Thread
import Image
#from PIL import Image

app = Flask('')

@app.route('/')
def home():
  
  #img = Image.open('./Images/JebWinsMasterminds.jpg')
  return 'Webserver Online, Discord Bot Online, Tylr is Dum'
  #return img

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()