import os
import sys
from loguru import logger
import psycopg2
import json
from psycopg2.extras import RealDictCursor

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
    self.connect(dbname)
    with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
      cur.execute(query)
      records = json.dumps(cur.fetchall())
      cur.close()
      return records

  def update_rows(self, query):
    self.connect()
    with self.conn.cursor() as cur:
      cur.execute(query)
      self.conn.commit()
      cur.close()
      return f"{cur.rowcount} rows affected."