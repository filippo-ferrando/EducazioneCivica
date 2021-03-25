import matplotlib.pyplot as plt
import csv
import numpy as np

year_co2 = []
total = []
gas_fuel = []
liquid_fuel = []
solid_fuel = []
cement = []
gas_flaring = []
pro_capite = []
year_anom = []
anomaly = []

file_co2 = open("CO2_emissions.csv")
file_anom = open("Temperature_Anomaly.csv")

reader_co2 = csv.reader(file_co2, delimiter=',')
reader_anom = csv.reader(file_anom, delimiter=',')

next(reader_co2)
for i in range(5):
    next(reader_anom)

for row in reader_co2:
    if int(row[0]) >= 1880:
        year_co2.append(int(row[0]))
        total.append(float(row[1]))
        gas_fuel.append(float(row[2]))
        liquid_fuel.append(float(row[3]))
        solid_fuel.append(float(row[4]))
        cement.append(float(row[5]))
        gas_flaring.append(float(row[6]))
        #pro_capite.append(float(row[7]))

for row in reader_anom:
    if int(row[0]) <= 2010:
        year_anom.append(int(row[0]))
        anomaly.append(float(row[1]))



fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1)

fig.suptitle("grafico")

ax1.plot(year_co2, total, '-g')
ax1.set_xlabel('Anno')
ax1.set_ylabel('Totale emissioni')

ax2.plot(year_anom, anomaly, '-r')
ax2.set_xlabel('Anno')
ax2.set_ylabel('Anomalie annue')

ax3.plot(year_anom, gas_fuel, '-y')
ax3.set_xlabel('Anno')
ax3.set_ylabel('Emissioni \n combustibile gassoso')

ax4.plot(year_anom, liquid_fuel, '--g')
ax4.set_xlabel('Anno')
ax4.set_ylabel('Emissioni \n combustibile fluido')

ax5.plot(year_anom, cement, '--y')
ax5.set_xlabel('Anno')
ax5.set_ylabel('Produzione cemento')

plt.tight_layout()
plt.show()