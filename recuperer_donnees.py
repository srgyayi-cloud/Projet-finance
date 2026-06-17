import yfinance as yf 

data = yf.download("AAPL", period="1mo")
print(data)
print (len(data))

# Suppression des valeurs manquantes 
data = data.dropna()

#Exploration des données 
print(data.info())
print(data.describe())

print ("Moyenne du prix de clôture :", data["Close"].mean())

print ("Prix le plus élevé :", data["High"].max())

print ("Prix le plus bas :", data["Low"].min())

# Sauvegarde des données sous format CSV
data.to_csv("AAPL_data.csv", index=False)

import psycopg2 

conn = psycopg2.connect(  host="localhost",  port=5432,  database="postgres",  user="postgres",  password="kurbyPostgres244") 

cursor = conn.cursor() 

for index, row in data.iterrows(): 
     cursor.execute("""  INSERT INTO cours_apple (date, open, high, low, close, volume)  
                    VALUES (%s, %s, %s, %s, %s, %s)  """, (index.date(), float(row["Open"]["AAPL"]), float(row["High"]["AAPL"]), float(row["Low"]["AAPL"]), float(row["Close"]["AAPL"]), int(row["Volume"]["AAPL"]))) 
conn.commit() 
cursor.close() 
conn.close() 
     
print("Données insérées avec succès")
