import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x ** 3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# 表格1
ax.scatter(x_values, y_values, s=5)
# 设置图表标题以及横纵坐标名称
ax.set_title("cubeNumber", fontsize=24)
ax.set_xlabel("Number", fontsize=14)
ax.set_ylabel("cubeOfNumber", fontsize=14)

# 表格2
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# 设置图表标题以及横纵坐标名称
ax.set_title("cubeNumber", fontsize=24)
ax.set_xlabel("Number", fontsize=14)
ax.set_ylabel("cubeOfNumber", fontsize=14)

plt.show()
