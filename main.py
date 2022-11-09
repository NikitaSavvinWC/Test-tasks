import psycopg2
from config import host, user, password, db_name
from generate import useres_table, purchases_table, items_table

userId = useres_table["userid"]
age = useres_table["age"]
purchaseid = purchases_table["purchaseid"]
itemid = purchases_table["itemid"]
date = purchases_table["date"]
price = items_table["price"]

con = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)
cur = con.cursor()

# cur.execute(
#             """CREATE TABLE Users(
#                 id serial PRIMARY KEY,
#                 userId INT NOT NULL,
#                 age INT NOT NULL);"""
# )
# cur.execute(
#             """CREATE TABLE Purchases (
#                 id serial PRIMARY KEY,
#                 purchaseId INT NOT NULL,
#                 userId INT NOT NULL,
#                 itemId INT NOT NULL,
#                 date DATE NOT NULL);"""
#         )
#cur.execute(
#             """CREATE TABLE Items(
#                 id serial PRIMARY KEY,
#                 itemId INT NOT NULL,
#                 price INT NOT NULL);"""
#         )

#con.commit()

#insert_query_users = """INSERT INTO Users (userId, age)
#             VALUES (%s, %s) ;"""
#for i in range(len(userId)):
#    record_users = (userId[i], age[i])
#    cur.execute(insert_query_users, record_users)

#insert_query_purchases = """INSERT INTO Purchases (purchaseid, userid, itemid, date)
#            VALUES (%s, %s, %s, %s) ;"""
#for i in range(len(userId)):
#    record_purchases = (purchaseid[i], userId[i], itemid[i], date[i])
#    cur.execute(insert_query_purchases, record_purchases)

#insert_query_items = """INSERT INTO Items (itemid, price)
#             VALUES (%s, %s) ;"""
#for i in range(len(itemid)):
#    record_items = (itemid[i], price[i])
#    cur.execute(insert_query_items, record_items)




