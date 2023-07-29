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

for date1,prediction1,temp_max1,temp_min1,wind1,weather1 in myresult:
    date.append(date1)
    prediction.append(prediction1)
    temp_max.append(temp_max1)
    temp_min.append(temp_min1)
    wind.append(wind1)
    weather.append(weather1)

dic={'date1' : date, 
     'prediction1' : prediction, 
     'temp_max1' : temp_max, 
     'temp_min1': temp_min,
     'wind1' : wind,
     'weather1' : weather
     }

df=pd.DataFrame(dic)
#a= df.info()
#print(a)
print(df)
df_csv = df.to_csv('C:/Users/ksswa/OneDrive/Desktop/Projects/dataset.csv')



