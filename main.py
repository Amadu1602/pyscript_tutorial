import datetime as dt
import matplotlib.pyplot as plt, numpy as np

pyscript.write('date', dt.datetime.today().strftime('%A %d %B %Y'))
pyscript.write('name', 'Amadu Adam')

x = np.random.randn(1000)
y = np.random.randn(1000)

fig, ax = plt.subplots()
ax.scatter(x,y)
fig