import os
import sys
from loguru import logger
import psycopg2

class Database:
  def __init__(self):
    self.host = os.getenv('DATABASE_HOST')
    self.username = os.getenv('DATABASE_USERNAME')
    self.password = os.getenv('USER_PASSWORD')
    self.port = os.getenv('DATABASE_PORT')
    self.conn = None

  def connect(self):
    if self.conn is None:
      try:
        self.conn = psycopg2.connect(host=self.host,
                                      user=self.username,
                                      password=self.password,
                                      port=self.port)
      except psycopg2.DatabaseError as e:
        logger.error(e)
        sys.exit()
      finally:
        logger.info('Connection opened successfully.')

  def select_rows(self, query):
    """Run a SQL query to select rows from table."""
    self.connect()
    with self.conn.cursor() as cur:
      cur.execute(query)
      records = [row for row in cur.fetchall()]
      cur.close()
      print('records', records)
      # return records

  def update_rows(self, query):
    """Run a SQL query to update rows in table."""
    self.connect()
    with self.conn.cursor() as cur:
      cur.execute(query)
      self.conn.commit()
      cur.close()
      return f"{cur.rowcount} rows affected."