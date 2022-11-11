from datetime import datetime
from random import randint

useres_table = {}
purchases_table = {}
items_table = {}
userid = []
age = []
purchaseid = []
itemid = []
date = []
price = []
thirty_day_mounts = [4, 6, 9, 11]
april_mount = 2
count_users = 1000 # 100 Count unique bayers
count_purchases = 100000  # 10000 Count purchases
count_items = 25 # Count unique products
def random_date(start_yesr, end_yesr):
    year_random = randint(start_yesr, end_yesr)
    month_random = randint(1, 12)
    if month_random == april_mount:
        if (year_random % 4) == 0: # Check on leap year
            day_random = randint(1, 29)
        else:
            day_random = randint(1, 28)
    elif month_random in thirty_day_mounts:
        day_random = randint(1, 30)
    else:
        day_random = randint(1, 31)
    data = datetime(year_random, month_random, day_random).isoformat()
    return data

def generate_users_table(count_data):
    for i in range(count_data):
        userid.append(1000000+i) # 1000 users
        age.append(randint(15, 65))
    useres_table = {
        "userid" : userid,
        "age" : age
    }
    return useres_table

useres_table = generate_users_table(count_users) # generate 1000 users
def generate_items_table(count_data):
    for i in range(count_data):
        itemid.append(20000+i)
        price.append(randint(100, 5000))
    items_table = {
        "itemid" : itemid,
        "price": price
    }
    return items_table

items_table = generate_items_table(count_items) # Сгенерировано 25 товаров

def generate_purchases_table(count_data, useres_table, items_table):
    userid = []
    itemid = []
    for i in range(count_data):
        purchaseid.append(3000000 + i)
        userid.append(randint(useres_table["userid"][0], useres_table["userid"][-1]))
        itemid.append(randint(items_table["itemid"][0], items_table["itemid"][-1]))
        date.append(random_date(2010, 2022))

    purchases_table = {
        "purchaseid" : purchaseid,
        "userid" : userid,
        "itemid" : itemid,
        "date" : date
    }
    return purchases_table

purchases_table = generate_purchases_table(count_purchases, useres_table, items_table) # Сгенерировано 100000 покупок
