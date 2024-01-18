import mysql.connector
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

import os
password_var = os.getenv("MYSQL_PASSWORD")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=password_var,
  database="data"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, email, id FROM users")

myresult = mycursor.fetchall()

df = pd.DataFrame(myresult, columns=['name', 'email', 'id'])

print(df)
