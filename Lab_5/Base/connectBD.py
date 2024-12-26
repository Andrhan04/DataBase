import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os

conn = psycopg2.connect(dbname = "LAB_0",
                         user="postgres",
                        password="pass",
                        host="127.0.0.1",
                        port="5432")