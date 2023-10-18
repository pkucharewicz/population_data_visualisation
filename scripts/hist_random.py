import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

df=pd.read_csv('final_population_data.csv')
random_col=df.columns[-2]
random_country=random_col.split("_")[-2]
year=random_col.split("_")[-1]

df = df.sort_values(by=random_col).iloc[:5]

population = np.array(df.iloc[:,4:-5])/10**6
names = np.array(df.iloc[:,0])
codes = np.array(df.iloc[:,1])

fig, ax = plt.subplots(figsize=(15, 10))

colors = [plt.cm.Dark2(i) for i in range(len(names))]
max_popul=np.max(population)
margin=0.1*np.max(population)
x_lim=max_popul+margin
plt.rcParams['font.size'] = '20'
def animate(i):
  ax.clear()
  ax.set_title('Population by year', pad=20)
  ax.set_ylabel('Frequency',fontsize=20, labelpad=20)
  ax.set_xlabel('Population size [mln]',fontsize=20, labelpad=20)
  ax.set_ylim(0,5)
  ax.set_xlim(0, x_lim)
  ax.text(0.95,0.95,str(1960+i),dict(size=30),horizontalalignment='right', verticalalignment='top',transform=ax.transAxes)
  population_vals=[[population[j][i]] for j in range(5)]
  ax.hist(population_vals,color=colors, label = names, width=1,stacked=True)
  ax.legend(loc='upper left')
plt.subplots_adjust(bottom=0.15)
anim = FuncAnimation(fig, animate, frames = len(population[0])-1, interval = 1)
anim.save("plots/hist_Random.gif")