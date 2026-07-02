import random
import datetime

products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 'Webcam', 'Printer', 'Scanner']

cities = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Hyderabad', 'Pune', 'Kolkata', 'Ahmedabad']

customers = [f'CUST{str(i).zfill(5)}' for i in range(1, 1001)]

start_date = datetime.date(2024, 1, 1)
end_date = datetime.date(2024, 12, 31)

date_range = (end_date - start_date).days

for i in range(50000):
    date = start_date + datetime.timedelta(days=random.randint(0, date_range))
    product = random.choice(products)
    price = round(random.uniform(100, 5000), 2)
    city = random.choice(cities)
    customer = random.choice(customers)
    quantity = random.randint(1, 5)

    print(f"{date},{product},{price},{city},{customer},{quantity}")
