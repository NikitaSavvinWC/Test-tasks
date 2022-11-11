import psycopg2
from config import *
from generate import useres_table, purchases_table, items_table


con = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)
cur = con.cursor()
def create_tables():
     cur.execute(
                 """CREATE TABLE Users(
                     id serial PRIMARY KEY,
                     userId INT NOT NULL,
                     age INT NOT NULL);"""
     )
     cur.execute(
                 """CREATE TABLE Purchases (
                     id serial PRIMARY KEY,
                     purchaseId INT NOT NULL,
                     userId INT NOT NULL,
                     itemId INT NOT NULL,
                     date DATE NOT NULL);"""
     )
     cur.execute(
                 """CREATE TABLE Items(
                     id serial PRIMARY KEY,
                     itemId INT NOT NULL,
                     price INT NOT NULL);"""
    )

     con.commit()
def filling_tables():
    insert_query_users = """INSERT INTO Users (userId, age)
                 VALUES (%s, %s) ;"""

    insert_query_purchases = """INSERT INTO Purchases (purchaseid, userid, itemid, date)
            VALUES (%s, %s, %s, %s) ;"""

    insert_query_items = """INSERT INTO Items (itemid, price)
             VALUES (%s, %s) ;"""

    for i in range(len(useres_table["userid"])):
        record_users = (useres_table["userid"][i], useres_table["age"][i])
        cur.execute(insert_query_users, record_users)


    for i in range(len(purchases_table["purchaseid"])):
        record_purchases = (
            purchases_table["purchaseid"][i],
            purchases_table["userid"][i],
            purchases_table["itemid"][i],
            purchases_table["date"][i]
        )

        cur.execute(insert_query_purchases, record_purchases)

    for i in range(len(items_table["itemid"])):
        record_items = (items_table["itemid"][i], items_table["price"][i])
        cur.execute(insert_query_items, record_items)

    con.commit()


print('Чтобы создать и заполнить таблицы данным useres, purchases, items введите 1')
action = int(input('Введите действие - '))

if action == 1:
    create_tables()
    filling_tables()
    print('Процесс выполнен')

