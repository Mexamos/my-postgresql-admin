from flask import Flask, request
from model import Database

app = Flask(__name__)
db = Database()

@app.route("/")
def hello():

  db.select_rows('SELECT datname FROM pg_database;')
  return "Hello World!"

@app.route("/name/<name>")
def get_book_name(name):
  return "name : {}".format(name)

@app.route("/details")
def get_book_details():
  # author=request.args.get('author')
  # published=request.args.get('published')
  # return "Author : {}, Published: {}".format(author,published)
  db.select_rows("SELECT table_schema, table_name, table_type FROM information_schema.tables WHERE table_catalog = 'demo' ORDER BY table_schema, table_name;", dbname='demo')
  return "Details !"

if __name__ == '__main__':
  app.run()