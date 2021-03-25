import matplotlib.pyplot as plt
import csv

mese_n = []
temperatura_m = []
giorni_giacca = []
giorni_scuola = []
giorni_videogiochi = []

file = open("dati.csv")
reader = csv.reader(file, delimiter=',')
next(reader)

for row in reader:
    mese_n.append(int(row[0]))
    temperatura_m.append(float(row[1]))
    giorni_giacca.append(int(row[2]))
    giorni_scuola.append(int(row[3]))
    giorni_videogiochi.append(int(row[4]))

#plt.figure(figsize = (50, 50))

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
#fig.subplots_adjust(hspace=0.1, wspace=0.1)
fig.suptitle("grafico")

ax1.plot(mese_n, temperatura_m, 'o-g')
ax1.set_xlabel('Mese')
ax1.set_ylabel('Temperatura')

ax2.plot(mese_n, giorni_giacca, 'o-r')
ax2.set_xlabel('Mese')
ax2.set_ylabel('Giorni con la giacca')

ax3.plot(mese_n, giorni_scuola, 'o-b')
ax3.set_xlabel('Mese')
ax3.set_ylabel('Giorni scolastici')

ax4.plot(mese_n, giorni_videogiochi, 'o-r')
ax4.set_xlabel('Mese')
ax4.set_ylabel('Giorni dove gioco')

plt.show()