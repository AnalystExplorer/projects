import pandas as pd 
import mysql.connector
import warnings

warnings.filterwarnings('ignore')
conn= mysql.connector.connect(
    host='localhost', 
    password = 'root', 
    user='root',
    database='python_sql'
    )

mycursor = conn.cursor()

mycursor.execute("SELECT * FROM python_sql.`seattle-weather (1)`")
myresult = mycursor.fetchall()

date = []
prediction = []
temp_max = []
temp_min = []
wind = []
weather = []

for Date,Precipitation,Temp_max,Temp_min,Wind,Weather in myresult:
    date.append(Date)
    prediction.append(Precipitation)
    temp_max.append(Temp_max)
    temp_min.append(Temp_min)
    wind.append(Wind)
    weather.append(Weather)

dic={'Date' : date, 
     'Precipitation' : prediction, 
     'Temp_max' : temp_max, 
     'Temp_min': temp_min,
     'Wind' : wind,
     'Weather' : weather
     }

df=pd.DataFrame(dic)
#a= df.info()
#print(a)
print(df)
df_csv = df.to_csv('C:/Users/ksswa/OneDrive/Desktop/Projects/dataset.csv')



