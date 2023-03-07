import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data Setting
x_labels = ['Car', 'Truck', 'Bus', 'Trailer', 'C.V.', 'Ped.', 'Motor.', 'Bicycle', 'T.C.', 'Barrier']
y_FSD = np.array([83.9, 56.4, 73.4, 41.4, 27.4, 84.3, 69.5, 55.6, 72.4, 60.7])
y_FSF = np.array([86.1, 62.5, 76.8, 44.8, 34.4, 88.6, 78.7, 73.7, 82.6, 75.5])
delta = y_FSF - y_FSD
assert len(y_FSD) == len(y_FSF)
df = pd.DataFrame({'FSD': y_FSD, 'FSF': y_FSF, 'delta': delta, 'labels': x_labels})

# Drawing
plt.rc('font', family='Times New Roman')
sns.set_style("whitegrid")
sns.barplot(df, x='labels', y='FSF', color='tomato', saturation=0.9, label='FSF')
ax = sns.barplot(df, x='labels', y='FSD', color=(163 / 255, 218 / 255, 222 / 255), saturation=0.9, label='FSD')
ax.axes.yaxis.set_ticklabels([])
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.bar_label(ax.containers[1], padding=-13, color='white', family='Times New Roman')
for index, row in df.iterrows():
    ax.text(row.name, row.FSF, '+' + str(round(row.delta, 2)), ha='center',
            position=(row.name, row.FSF + 0.5), family='Times New Roman')
plt.legend(bbox_to_anchor=(0.4, 1), prop='Times New Roman')
plt.title('mAP Comparison between FSD and FSF', fontweight='bold', family='Times New Roman')
plt.xlabel(None)
plt.xticks(fontproperties='Times New Roman')
plt.ylabel(None)
plt.ylim((24, 95))
plt.savefig("mAP.pdf", dpi=1024)
plt.show()
