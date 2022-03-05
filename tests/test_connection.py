#!/usr/local/miniconda3/envs/postgres-3.6/bin/python

import psycopg2

conn = psycopg2.connect(
        database='postgres',
        user='postgres',
        password='abc123',
        host='127.0.0.1',
        port='5432')
conn.close()

print('Connected to database successfully')
