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
years = np.arange(1960,2023,1)
fig, ax = plt.subplots(figsize=(15, 10))
plt.rcParams['font.size'] = '20'
colors = [plt.cm.Dark2(i) for i in range(len(names))]
max_popul=np.max(population)
margin=0.2*np.max(population)

def animate(i):
  ax.clear()
  ax.set_title('Population by year', pad=20)
  ax.set_ylabel('Population size [mln]',fontsize=20, labelpad=20)
  ax.set_xlabel('Year',fontsize=20, labelpad=20)
  ax.set_xlim(1960, 2022)
  ax.set_ylim(0,max_popul+margin)
  ax.text(0.95,0.95,str(1960+i),dict(size=30),horizontalalignment='right', verticalalignment='top',transform=ax.transAxes)

  ax.plot(years[:i],population[0][:i],color=colors[0],label=names[0])
  ax.plot(years[:i],population[1][:i],color=colors[1],label=names[1])
  ax.plot(years[:i],population[2][:i],color=colors[2],label=names[2])
  ax.plot(years[:i],population[3][:i],color=colors[3],label=names[3])
  ax.plot(years[:i],population[4][:i],color=colors[4],label=names[4])
  ax.legend(loc='upper left')

  for j in range(5):
    if i>2:
      ax.annotate(codes[j], xy=(years[i-1], population[j][i-1]), xytext = (years[i-1]-2, population[j][i-1]+margin/10),fontsize=15)
    elif i==1 or i==2:
      ax.annotate(codes[j], xy=(years[i-1], population[j][i-1]), xytext = (years[0], population[j][i-1]+margin/10),fontsize=15)


anim = FuncAnimation(fig, animate, frames = len(population[0]), interval = 1)
anim.save("plots/line_most_populated.gif")