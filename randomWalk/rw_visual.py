import matplotlib.pyplot as plt

from randomWalk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)

    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
               edgecolors='none', s=100)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
               cmap=plt.cm.Blues, edgecolors='none', s=15)
    plt.show()

    keep_running = input("Make another walk? y/n:")
    if keep_running == 'n':
        break
