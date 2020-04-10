from flask import Flask, request
from flask_cors import CORS
from model import Database

app = Flask(__name__)
CORS(app, origins='*', supports_credentials=True)

db = Database()

@app.route("/databases")
def get_data_bases():
  database_list = db.select_rows('SELECT datname FROM pg_database;')
  print('database_list', database_list)
  return database_list

@app.route("/databases/<dbname>/tables")
def get_table_list(dbname):
  tables_list = db.select_rows("SELECT table_schema, table_name, table_type FROM information_schema.tables WHERE table_catalog = '" + dbname + "' ORDER BY table_schema, table_name;", dbname=dbname)
  return tables_list

@app.route("/databases/<dbname>/schema/<schemaname>")
def get_schema(dbname, schemaname):
  schema_table_list = db.select_rows("SELECT c.table_name, t.table_type, json_agg(json_build_object('column_name', c.column_name, 'data_type', c.data_type)) AS columns FROM information_schema.columns c JOIN information_schema.tables t ON c.table_name = t.table_name WHERE c.table_schema = '" + schemaname + "' GROUP BY c.table_name, t.table_type;", dbname=dbname)
  return schema_table_list

@app.route("/databases/<dbname>/schema/<schemaname>/tables/<tablename>")
def get_relation(dbname, schemaname, tablename):
  relation = db.select_rows("SELECT column_name, data_type FROM information_schema.columns WHERE table_schema = '" + schemaname + "' AND table_name = '" + tablename + "';", dbname=dbname)
  return relation

if __name__ == '__main__':
  app.run()