from flask import Flask, request, jsonify
from flask_cors import CORS
from model import Database

app = Flask(__name__)
CORS(app, origins='*', supports_credentials=True)

db = Database()

@app.route("/databases")
def hello():
  database_list = db.select_rows('SELECT datname FROM pg_database;')
  print('database_list', database_list)
  return jsonify(database_list)

@app.route("/databases/<dbname>/tables")
def get_book_details(dbname):
  db.select_rows("SELECT table_schema, table_name, table_type FROM information_schema.tables WHERE table_catalog = '" + dbname + "' ORDER BY table_schema, table_name;", dbname=dbname)
  return "Details !"

if __name__ == '__main__':
  app.run()