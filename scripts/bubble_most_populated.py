import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import matplotlib.colors

df=pd.read_csv('final_population_data.csv')
df = df.sort_values(by='2021',ascending=False).iloc[:5]

population = np.array(df.iloc[:,4:-5])
names = np.array(df.iloc[:,0])
codes = np.array(df.iloc[:,1])
area = np.array(df['area'])
years = np.arange(1960,2023,1)
fig, ax = plt.subplots(figsize=(15, 10))
colors = [plt.cm.Dark2(i) for i in range(len(names))]
plt.rcParams['font.size'] = '20'

density = [population[i]/area[i] for i in range(5)]
max_dens=np.max(density)
min_dens=np.min(density)
population = population/10**6
max_popul=np.max(population)

# markers for a size legend
labels=[max_dens,(max_dens+min_dens)/2,min_dens]
markers=[]
for i in labels:
    markers.append(plt.scatter([],[], s=i*20,c='lightgrey',edgecolor='black'))
labels = [round(i) for i in labels]

#markers for a color legend

markers_colors=[]
for i in range(len(names)):
    markers_colors.append(plt.scatter([],[], s=100,c=[colors[i]], label=names[i], cmap='Dark2',alpha=0.5))

margin=0.25*np.max(population)
def animate(i):
    ax.clear()
    ax.set_title('Population by year', pad=20)
    ax.set_ylabel('Population size [mln]',fontsize=20, labelpad=20)
    ax.set_xlabel('Year',fontsize=20, labelpad=20)
    ax.set_xlim(1960, 2025)
    ax.set_ylim(0,max_popul+margin)
    ax.text(0.95,0.95,str(1960+i),dict(size=30),horizontalalignment='right', verticalalignment='top',transform=ax.transAxes)
    x=[years[i]]*5
    y=[population[j][i] for j in range(5)]
    a=[density[j][i]*20 for j in range(5)]
    ax.scatter(x, y, c=colors, s=a, alpha=0.5, label=names, cmap='Dark2')

    legend = ax.legend(handles=markers_colors, loc='upper center',title_fontsize=15,fontsize=15)
    # legend1 = ax.legend(handles=markers,labels=names,
    #                     loc="lower left", title="Country")
    ax.add_artist(legend)
    legend1 = ax.legend(handles=markers, labels=labels, loc='upper left', title='Population density [people/km$^2$]',title_fontsize=15,handletextpad=2)
    legend1._legend_box.sep = 50

    for j in range(5):
        if i>2:
            ax.annotate(codes[j], xy=(years[i], population[j][i]), xytext = (years[i]-2, population[j][i]+margin/10),fontsize=15)
        elif i==1 or i==2:
            ax.annotate(codes[j], xy=(years[i], population[j][i]), xytext = (years[0], population[j][i]+margin/10),fontsize=15)

anim = FuncAnimation(fig, animate, frames = len(population[0]), interval = 1)
anim.save("plots/bubble_most_populated.gif")