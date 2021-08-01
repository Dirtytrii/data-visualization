import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x ** 2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='red', s=10)

# 设置图表标题以及横纵坐标名称
ax.set_title("squareNumber", fontsize=24)
ax.set_xlabel("Number", fontsize=14)
ax.set_ylabel("squareOfNumber", fontsize=14)

ax.axis([0, 1100, 0, 1100000])
plt.show()
