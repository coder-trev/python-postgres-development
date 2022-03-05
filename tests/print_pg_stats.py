#!/usr/local/miniconda3/envs/postgres-3.6/bin/python

import psycopg2

conn = psycopg2.connect(
        database='postgres',
        user='postgres',
        password='abc123',
        host='127.0.0.1',
        port='5432')

cur = conn.cursor()

cur.execute('SELECT usename,client_addr,client_port,query FROM pg_stat_activity')
for row in cur.fetchall():
    user, addr, port, query = row
    if query:
        print(f'{user}@{addr}:{port} ran "{query}"')

conn.close()
