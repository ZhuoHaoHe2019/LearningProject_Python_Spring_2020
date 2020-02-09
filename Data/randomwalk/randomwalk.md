#### 什么是 随机漫步图 ？
> 随机漫步是一种路径，这种路径每次行走都是完全随机的，没有明确的方向，结果是有一些列随机决策决定的。
> 我们可以把它当作蚂蚁在晕头转向的情况下，每次都沿着随机的方向行进所经过的路径。

在生活中的很多领域我们都可以用到随机漫步。
例如，漂浮在水滴上的划分因不断受到水分子的挤压而在水面上移动。
水滴中的分子运动是随机的，因此划分在水面上的运动路径犹如随机漫步。

接下来我们将一步一步的实现随机漫步。首先我们要先创建 `RandomWalk` 类。

```python
from random import choice

class RandomWalk():
    """一个随机生成漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步数据的属性"""
        self.num_points = num_points

        # 所有随机漫步都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]
```

在该类中包含三个属性，其中一个存储随机漫步的次数，在上面代码中次数为5000个。
另外两个是列表，分别存放随机漫步经过的每个点的x和y坐标，
在上述代码中规定所有的随机漫步都始于(0,0)。

---
接下来使用函数 `fill_walk()` 来生成漫步包含的点，并决定每次漫步的方向以及漫步的距离。

```python
from random import choice
    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步，直到列表到达指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
```
在函数中设置一个循环，让“蚂蚁”不断漫步，直到步数到达最大的设定。
使用 `choice()` 函数给 `x_direction` 选择一个值，结果是向右走（1）或是向左走（-1）,
同时用该函数为 `y_direction` 设置1~4中的一个值，来提供向方向的移动距离。

但如何确定“蚂蚁”移动的方向是上下还是左右呢?
> 我们建立在x,y二维坐标轴上。
> 
> x_step为正，则向右。而为负，则向左。
>
> y_step为正，则向上。而为负，则向下。

为了获取漫步中下一个点的x值和y值，我们可以将 `x/y_step + x/y_values` 得到新的位置。

不过，这个 `fill_walk()` 函数过于冗长，我们可以对他进行重构。

```python
    def get_step(self):
        """计算下一个随机漫步落点"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步，直到列表到达指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            x_step = self.get_step()

            y_step = self.get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
```

---

为了绘制出随机漫步的图像，我们可以使用函数 `scatter()`

```python
import matplotlib.pyplot as plt

from randomwalk import RandomWalk

# 创建一个RandomWalk实例，并将其包含的点都绘制出来
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=2)
plt.show()
```

![图1](C:\Users\wohez\Documents\GitHub\LearningProject_Python_Spring_2020\Data\randomwalk\1.jpg)

---

同时我们也可以对随机漫步的图表的特性进行修改，我们的目的是突出每次漫步的重要特征，并让分散注意力的元素不显得那么显眼。

对于颜色：

我们可以使用颜色映射来指出漫步中各点的先后顺序，让漫步的顺序更加清晰。

```python
point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolors='none', s=10)
```
`point_numbers` 是一个0~5000的列表，用来记忆各个点出现的顺序，当作参数传入函数`scatter()`。

对于坐标轴：

我们要隐藏坐标轴，因为坐标轴在有些随机漫步的图表中并不重要。
只需要两条语句，设置 `set_visible()` 为 *False*

```python
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
```