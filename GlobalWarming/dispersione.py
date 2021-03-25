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

fig, (ax1) = plt.subplots(1)