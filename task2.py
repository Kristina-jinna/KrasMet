import psycopg2
import sys

conn = None

def numberRequest(i):
    if i == 1:
       query = 'select u.name as user_name, c2.amount as amount_computer from  "User" u, (select count(c.comp_name) amount, id_user from "Computer" c group by c.id_user order by c.id_user) c2 where u.id = c2.id_user;'
    elif i == 2:
        query = 'select u.name as user_name from  "User" u where u.id not in (select c.id_user from "Computer" c) order by u.name;'
    elif i == 3:
        query = 'select u.name as user_name, c2.amount as amount_computer from  "User" u, (select count(c.comp_name) amount, id_user, rank() OVER (ORDER BY count(c.comp_name) DESC) AS rank from "Computer" c group by c.id_user) c2 where u.id = c2.id_user and c2.rank =1;'
    else:
        print("Not exist")
        exit()
    return query

try:
    conn = psycopg2.connect(dbname='TestKrasMet', user='postgres', password='123', host='localhost')
    cursor = conn.cursor()
    cursor.execute(numberRequest(3))
    records = cursor.fetchall()
    print(records)

except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    sys.exit(1)

finally:
    if conn:
        conn.close()