from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
max_result = die_1.num_sides + die_2.num_sides
frequencies = []
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

# dtick表示刻度上的显示频率，如下使用为显示间隔为一
x_axis_config = {'title': '结果', 'dtick': 1}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title='掷一个d6和一个d10 50 000次的结果',
                   xaxis=x_axis_config, yaxis=y_axis_config)
# 生成保存文件
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')
