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
count_data = 10  # It is count data for generate test data

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

def generate_data(count_data):
    for i in range(count_data):
        userid.append(randint(1, 10000))
        age.append(randint(16, 40))
        purchaseid.append(randint(20000, 29999))
        itemid.append(randint(30000, 39999))
        date.append(random_date(2000, 2022))
        price.append(randint(100, 5000))

    useres_table = {
        "userid" : userid,
        "age" : age
    }
    purchases_table = {
        "purchaseid" : purchaseid,
        "userid" : userid,
        "itemid" : itemid,
        "date" : date
    }
    items_table = {
        "itemid" : itemid,
        "price": price
    }
    return useres_table, purchases_table, items_table

useres_table, purchases_table, items_table = generate_data(count_data)
