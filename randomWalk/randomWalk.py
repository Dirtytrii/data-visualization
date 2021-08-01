from random import choice


class RandomWalk:
    """一个可以生成随机步数的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性。 """
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """实现随机漫步"""

        # 不断漫步直到列表达到指定长度
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        direction = choice([1, -1])
        distances = choice(range(10))
        step = distances * direction

        return step
