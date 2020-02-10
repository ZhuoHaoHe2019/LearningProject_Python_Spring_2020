### 使用 Pygal 来模拟抛骰子

#### 什么是 Pygal ？

> Pygal 是 Python 的可视化包，用来生成可缩放的矢量图形文件。对于需要在尺寸不同的屏幕上显示的图表，使用 Pygal 绘制将很有用，
> 因为他们可以进行自动的缩放。

---

### 模拟骰子

对于骰子来说，我们可以创建一个Die类，来表示一个骰子。

```python
from random import randint

class Die():
    """表示一个骰子的类"""

    def __init__(self,num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机值"""
        return randint(1, self.num_sides)
```

方法 `roll()` 使用函数 `randint` 随机生成一个 1~面数之间的随机数，模拟动作抛骰子。

使用 Pygal 创建图表之前，我们先抛几次骰子来获得一些基础数据。

```python
from die import Die

# 创建一个D6（六面骰子）
die = Die()

# 抛几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

print(results)
```

在上面的代码中，我们抛了1000次骰子，作为接下来处理的基础数据。

> [4, 3, 6, 6, 5, 4, 4, 6, 2, 3, 3, 5, 6, 6, 3, 6, 3, 1, 1, 2,...]

接下来，对我们自己设计的数据来进行分析。为了分析我们设置的 Die 是否正确，我们对每一面出现的次数进行统计，
如果每一个面出现的次数相近，则表示我们创建的骰子类 Die 与我们生活中的骰子较为相似。

```python
frequencies = []

for value in range(1, die.num_sides):
    frequency = results.count(value)
    frequencies.append(frequency)
    
print(frequencies)
```
列表 `frequencies` 用于存储每种点数出现的次数，我们遍历可能的点数，用函数 `count()` 计算每种点数在结果中出现的次数。

> 列表 `freqencies` : [163, 162, 177, 177, 140, 181]

目测结果每个面出现的次数偏差不大，为了更直观的比较，我们将使用 Pygal 把数据做成可视化的形式。

```python
import pygal

--snip--

hist = pygal.Bar()

hist.title = 'Results of rolling one D6 1009 times.'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
```
`hist` 存储 `pygal.Bar()` 实例， 之后设置图像的各种其他信息。
之后我们使用 `add()` 将一系列值添加到图表中（向他传递要给添加的值指定的标签，还有一个列表，其中包含将出现在图表中的值）。

![图1](C:\Users\wohez\Documents\GitHub\LearningProject_Python_Spring_2020\Data\dice\1.jpg)

---

### 同时抛两个骰子

同时抛两个骰子，求两个骰子的点数和。这样的到的点数更多，结果分布情况也不同。
我们也通过简单修改上面的代码，实现同时抛两个骰子，并对两个骰子的数据结果可视化显示，来研究分布结果。

```python
from die import Die
import pygal

# 创建两个D6（六面骰子）
die_1 = Die()
die_2 = Die()

# 抛几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_reslut = die_1.num_sides + die_2.num_sides
for value in range(2, max_reslut + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = 'Results of rolling two D6 dice 1000 times.'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
```

![图2](C:\Users\wohez\Documents\GitHub\LearningProject_Python_Spring_2020\Data\dice\2.jpg)

---

#### 同时抛两个面数不同的骰子

接下来我们创建一个6面骰子和10面骰子，看看同时抛这两个骰子500000次的数据结果

```python
from die import Die
import pygal

# 创建两个D6（六面骰子）
die_1 = Die()
die_2 = Die(10)

# 抛几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_reslut = die_1.num_sides + die_2.num_sides
for value in range(2, max_reslut + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = 'Results of rolling a D6 and a D10 dice 50,000 times.'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')
```

![图3](C:\Users\wohez\Documents\GitHub\LearningProject_Python_Spring_2020\Data\dice\3.jpg)
