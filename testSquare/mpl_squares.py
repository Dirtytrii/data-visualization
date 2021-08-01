# coding:utf-8
import matplotlib.pyplot as plt

input_values = [0, 1, 2, 3, 4, 5]
squares = [0, 1, 4, 9, 16, 25]
plt.style.use('classic')
fig, ax = plt.subplots()

ax.plot(input_values, squares, linewidth=3)

# 设置图表标题以及横纵坐标名称
ax.set_title("squareNumber", fontsize=24)
ax.set_xlabel("Number", fontsize=14)
ax.set_ylabel("squareOfNumber", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

# show and savefig can not do at the same time
plt.savefig('myFirst_plot.png')
plt.show()
