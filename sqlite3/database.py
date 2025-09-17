# https://www.youtube.com/watch?v=byHcYRpMgI4

# import sqlite3

# # connect to database
# conn = sqlite3.connect('customer.db')
# # in-memory db
# #conn = sqlite3.connect(':memory:')

# # create a cursor
# cur = conn.cursor()

# # create a table
# cur.execute("""create table customers (
#     first_name text,
#     last_name text,
#     email text
#     )""")

# # datatypes:
# # null
# # integer
# # real
# # text
# # blob

# # commit our command
# conn.commit()

# # close our connection
# conn.close()

#============================================================

# import sqlite3

# conn = sqlite3.connect('customer.db')

# cur = conn.cursor()

# cur.execute("""INSERT INTO customers VALUES (
#     'John',
#     'Elder',
#     'john@codemy.com'
#     )""")

# many_customers = [
#                     ('Wes', 'Brown', 'wes@gmail.com'),
#                     ('Steph', 'Kuewa', 'steph@gmail.com'),
#                     ('Dan', 'Pas', 'dan@gmail.com'),
#                     ('Mary', 'Brown', 'mary@gmail.com'),
#                 ]

# cur.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# conn.commit()

# conn.close()

#============================================================

# import sqlite3

# conn = sqlite3.connect('customer.db')

# cur = conn.cursor()

# cur.execute("SELECT * FROM customers")
# #print(cur.fetchone())
# #print(cur.fetchmany(3))
# #print(cur.fetchall())

# items = cur.fetchall()
# for item in items:
#     print(item[0] + "\t" + item[1] + "\t" + item[2])

# conn.commit()

# conn.close()

#============================================================

# import sqlite3

# conn = sqlite3.connect('customer.db')
# cur = conn.cursor()

# cur.execute("SELECT * FROM customers WHERE last_name = 'Elder'")
# print(cur.fetchall())

# # % 기호를 와일드카드로 사용할 수 있다.
# cur.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%'")
# print(cur.fetchall())

# conn.commit()
# conn.close()

#============================================================

# import sqlite3

# conn = sqlite3.connect('customer.db')
# cur = conn.cursor()

# # Update Records
# cur.execute("""UPDATE customers SET first_name = 'John'
#     WHERE rowid = 1
#     """)

# conn.commit()

# cur.execute("SELECT rowid, * FROM customers")

# items = cur.fetchall()

# for item in items:
#     print(item)

# conn.close()

#============================================================

# import sqlite3

# conn = sqlite3.connect('customer.db')
# cur = conn.cursor()

# # Delete Records
# cur.execute("DELETE from customers WHERE rowid = 4")

# conn.commit()

# cur.execute("SELECT rowid, * FROM customers")

# items = cur.fetchall()

# for item in items:
#     print(item)

# conn.close()

#============================================================

# import sqlite3

# conn = sqlite3.connect('customer.db')
# cur = conn.cursor()

# # Query the database - ORDER BY
# # ASC = ascending = low to high
# # DESC = descending = high to low
# cur.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")

# items = cur.fetchall()

# for item in items:
#     print(item)

# conn.close()

#============================================================

# import sqlite3

# conn = sqlite3.connect('customer.db')
# cur = conn.cursor()

# # Query the database - AND/OR
# cur.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' AND rowid = 2")

# items = cur.fetchall()

# for item in items:
#     print(item)

# conn.close()

#============================================================

# import sqlite3

# conn = sqlite3.connect('customer.db')
# cur = conn.cursor()

# # Query the database - LIMIT
# cur.execute("SELECT rowid, * FROM customers LIMIT 2")

# items = cur.fetchall()

# for item in items:
#     print(item)

# conn.close()

#============================================================

# import sqlite3

# conn = sqlite3.connect('customer.db')
# cur = conn.cursor()

# # Drop Table
# cur.execute("DROP TABLE customers")
# conn.commit()

# cur.execute("SELECT rowid, * FROM customers")

# items = cur.fetchall()

# for item in items:
#     print(item)

# conn.close()

#============================================================

import sqlite3

# Query The DB and Return All Records
def show_all():
    conn = sqlite3.connect('customer.db')
    cur = conn.cursor()
    
    cur.execute("SELECT rowid, * from customers")
    items = cur.fetchall()

    print("\n----- RESULT: show_all -----")
    for item in items:
        print(f"{item[0]}\t{item[1]}\t{item[2]}")

    conn.commit()
    conn.close()

# Add A New Record To The Table
def add_one(first, last, email):
    conn = sqlite3.connect('customer.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

    conn.commit()
    conn.close()

# Add Many Records To Table
def add_many(list):
    conn = sqlite3.connect('customer.db')
    cur = conn.cursor()

    cur.executemany("INSERT INTO customers VALUES (?,?,?)", (list))

    conn.commit()
    conn.close()

# Delete Record from table
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    cur = conn.cursor()

    cur.execute("DELETE from customers WHERE rowid = (?)", id)

    conn.commit()
    conn.close()

# Lookup with Where
def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    cur = conn.cursor()

    cur.execute("SELECT rowid, * from customers WHERE email = (?)", (email,))

    items = cur.fetchall()

    print("\n----- RESULT: email_lookup -----")
    for item in items:
        print(f"{item[0]}\t{item[1]}\t{item[2]}")

    conn.commit()
    conn.close()

def create_table_customers():
    conn = sqlite3.connect('customer.db')
    cur = conn.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS customers (
                    first_name text,
                    last_name text,
                    email text
                )""")

    conn.commit()
    conn.close()

    print("\nCREATE TABLE: customers")

def drop_table_customers():
    conn = sqlite3.connect('customer.db')
    cur = conn.cursor()

    cur.execute("DROP TABLE customers")

    conn.commit()
    conn.close()

    print("\nDROP TABLE: customers")