import os
import sys
from loguru import logger
import psycopg2

from psycopg2.extras import DictCursor

class Database:
  def __init__(self):
    self.host = os.getenv('DATABASE_HOST')
    self.username = os.getenv('DATABASE_USERNAME')
    self.password = os.getenv('USER_PASSWORD')
    self.port = os.getenv('DATABASE_PORT')
    self.conn = None
    self.dbname = None

  def connect(self, dbname=''):
    if self.conn is None or dbname != self.dbname:
      try:
        self.dbname = dbname
        self.conn = psycopg2.connect(host=self.host,
                                      user=self.username,
                                      password=self.password,
                                      port=self.port,
                                      database=dbname)
      except psycopg2.DatabaseError as e:
        logger.error(e)
        sys.exit()
      finally:
        logger.info('Connection opened successfully.')

  def select_rows(self, query, dbname=''):
    """Run a SQL query to select rows from table."""
    self.connect(dbname)
    with self.conn.cursor() as cur:
      print('query', query)
      cur.execute(query)
      print('cur.fetchall()', cur.fetchall())
      # records = [row[0] for row in cur.fetchall()]
      # print('records', records)
      cur.close()
      # return records
  
  def select_rows_dict_cursor(self, query):
    """Run a SQL query to select rows from table and return dictionarys."""
    self.connect()
    with self.conn.cursor(cursor_factory=DictCursor) as cur:
      cur.execute(query)
      print('cur.fetchall()', cur.fetchall())
      for row in cur.fetchall():
        # logger.info(row)
        print('row', row)

  def update_rows(self, query):
    """Run a SQL query to update rows in table."""
    self.connect()
    with self.conn.cursor() as cur:
      cur.execute(query)
      self.conn.commit()
      cur.close()
      return f"{cur.rowcount} rows affected."