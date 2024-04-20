import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
bottom = np.zeros(5)

players = ['Haliburton', 'Young', 'VanVleet', 'Jokic', 'Ball']
assists = [12.0, 10.8, 9.3, 8.7, 8.3]
bar_labels = ['red', 'blue', '_red', 'orange', 'green']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
for assist in assists:
    p = ax.bar(players,assists, label = bar_labels, color = bar_colors)
    bottom += assist
    ax.bar_label(p, label_type = 'center')

ax.set_ylabel('Asists Per Game \n(APG)')
ax.set_title('Top passers in the NBA')

plt.show()