import sqlite3
import matplotlib.pyplot as plt

db_connection = sqlite3.connect('climate.db')

cursor = db_connection.cursor()

co2_query = "SELECT Year, CO2, Temperature FROM ClimateData"

cursor.execute(co2_query)
data = cursor.fetchall()

years, co2, temp = zip(*data)

cursor.close()
db_connection.close()

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")

plt.show()
plt.savefig("co2_temp_1.png")
