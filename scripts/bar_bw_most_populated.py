import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

df=pd.read_csv('final_population_data.csv')
df = df.sort_values(by='2021',ascending=False).iloc[:5]

population = np.array(df.iloc[:,4:-5])/10**6
names = np.array(df.iloc[:,0])
codes = np.array(df.iloc[:,1])

fig, ax = plt.subplots(figsize=(15, 10))
plt.rcParams['font.size'] = '20'

colors = [plt.cm.Dark2(i) for i in range(len(names))]
max_popul=np.max(population)
margin=0.1*np.max(population)
y_lim=max_popul+margin
def animate(i):
    ax.clear()
    ax.set_title('Population by year', pad=20)
    ax.set_ylabel('Population size [mln]',fontsize=20, labelpad=20)
    ax.set_xlabel('5 most populated countries',fontsize=20, labelpad=30)
    plt.xticks(fontsize=15)
    ax.set_ylim(0, y_lim)
    ax.text(0.95,0.95,str(1960+i),dict(size=30),horizontalalignment='right', verticalalignment='top',transform=ax.transAxes)
    population_vals=[population[j][i] for j in range(5)]
    rects = ax.bar(names,population_vals, color='w', edgecolor='black', hatch=['--', '..', '||', '\\','xx'])
    ax.bar_label(rects,labels=codes)
plt.subplots_adjust(bottom=0.15)
anim = FuncAnimation(fig, animate, frames = len(population[0])-1, interval = 1)
anim.save("plots/bar_most_populated_bw.gif")