from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello world!"

@app.route("/index")
def index():
  return "Index Page"

@app.route("/about")
def about():
  return "About Page"

if __name__ == '__main__':
  app.run()