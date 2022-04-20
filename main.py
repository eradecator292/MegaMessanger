import pandas as pd
import pymysql.cursors
import matplotlib.pyplot as plt

# Подключение к базе данных:
connection = pymysql.connect(host = '127.0.0.1',
user = 'root',
password = 'bofabo72',
db ='DB', # название базы данных
charset ='utf8mb4',
cursorclass = pymysql.cursors.DictCursor)
with connection.cursor() as cursor:
    sql = "SELECT * from Tour"
    cursor.execute(sql)
    rows = cursor.fetchall()
    df2 = pd.DataFrame(rows)
print(df2)



with connection.cursor() as cursor:
    sql = "SELECT * FROM Hotel ORDER BY HotelType"
    cursor.execute(sql)
    rows = cursor.fetchall()
    df = pd.DataFrame(rows)
    connection.close()
print(df)

