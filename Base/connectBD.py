import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(dbname = "postgres",
                         user="postgres",
                        password="pass",
                        host="127.0.0.1",
                        port="5432")

