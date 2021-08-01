import matplotlib.pyplot as plt

x_values = [0, 1, 2, 3, 4, 5]
y_values = [0, 1, 4, 9, 16, 25]

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# 设置图表标题以及横纵坐标名称
ax.set_title("squareNumber", fontsize=24)
ax.set_xlabel("Number", fontsize=14)
ax.set_ylabel("squareOfNumber", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
