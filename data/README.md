[toc]



#### 什么是 *matplotlib* ？

***

*matplotlib* 是一个数学绘图库， 我们可以用它来制作一些简单的图表，例如折线图，或散点图。

### 绘制简单的折线图

```python
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares)
plt.show()
```

模块 `pyplot` 包含很多用于生成图表的函数， 类似于 *matlab*

把列表作为参数传入函数 `pyplot.plot()`, 
这个函数会尝试根据这些数字绘制出有意义的图形。

函数 `pyplot.show()` 会打开图像查看器，并显示绘制的图形。查看器可以实现放大缩小或者保存功能。

![图1](C:\Users\wohez\Desktop\Python\matplotlib\1.jpg)

在画出了一个简单的图标之后，我们可以对图表进行简单的改动，来增加图形的可读行，如修改标签文字和线条粗细。

```python
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)

# 设置图标标题， 并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=14)

plt.show()
```

在代码中, `linewidth` 决定了 `plot()` 绘制的线条的粗细。 函数 `title()` 给图标指定标题。 
参数 `fontsize` 代表图表中文字的大小。

函数 `xlabel()` 和 函数 `ylabel()` 可以设定每条轴线的标题，而函数 `tick_params()` 设置刻度的样式，
其中指定的实参可以设置x轴和y轴上的刻度。

再完成了这些设置之后，就会发现图形的可读性有了一点提高。

![图2](C:\Users\wohez\Desktop\Python\matplotlib\2.jpg)

但是，如果我们自习观察图表，我们会发现，图中的数据并不是完全正确的，例如图中4的平放式25.

这事由于绘图工具plot的一些默认设置导致的问题。 如，plot的默认原点x=0，但是我们这个例子中要求的原点x=1

为了改变这种默认的设置，我们可以添加输入值和输出值

```python
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)
```

![图3](C:\Users\wohez\Desktop\Python\matplotlib\3.jpg)

这样一来我们就可以实现正确的绘制一个简单的折线图

---

---



### 绘制简单的散点图

有时我们需要绘制散点图来处理离散的数据，所以我们就可以利用函数 `scatter()` 来绘制简单的散点图.

```python
import matplotlib.pyplot as plt

plt.scatter(2, 4)
plt.show()
```

利用简单的两行语句就可实现一个散点的绘制，同时我们也可以对代码进行修改来设置输出的样式，使得散点图更具有可读性。

```python
import matplotlib.pyplot as plt

plt.scatter(2, 4, s=200)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
```

在设置了各项参数之后，我们就可以得到一个较为完整的散点图了。

<img src="C:\Users\wohez\Desktop\Python\matplotlib\4.jpg" alt="图4" style="zoom:50%;" />

不过，我们在数据处理时，大多数情况下都是要处理的是大量的数据，而不是只有一个离散的点，所以我们需要使用函数绘制一些列的点。

通过 `列表` 来给函数传输一系列的点

```python
import matplotlib.pyplot as plt
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s=200)

--snip--
```

函数 `scatter()` 分别从 `x_value` 和 `y_value` 读取一个值来绘制一个点 (x,y)。

![图5](C:\Users\wohez\Desktop\Python\matplotlib\5.jpg)

手工输入或手工计算列表中所有的值，在数据量很大的时候效率会非常的低。我们可以使用循环来代替我们完成计算。

```python
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]
plt.scatter(x_values, y_values, s=1)

--snip--

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()
```

利用函数 `range()` 创建数字1~1000的列表，遍历x的值并计算 `x**2` ,并将其结果存储到列表 `y_values` 中。

函数 `axis()` 指定每个坐标轴的取值范围。向函数中传入四个参数，x、y的最大值最小值。

这样我们就可以让循环来帮助我们计算大量的数据并绘图了。

![图6](C:\Users\wohez\Desktop\Python\matplotlib\6.jpg)

`matplotlib` 默认散点图中的点为蓝色点和黑色轮廓，但是在数据过多时我们会发现。黑色轮廓会粘连在一起。
不过我们可以通过改变一些参数来修改一些外观。

```python
plt.scatter(x_values, y_values, edgecolors='none', s=40)
```

这样一来就会发现图中将时蓝色的实心点。

当然我们也可以修改数据点的颜色。

```python
plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)

# 也可以使用RGB来设置自定义颜色
plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolors='none', s=40)
```

为了使图表的可读性更强，也更漂亮，我们可以使用颜色映射(colormap)是一些列颜色，从其实颜色渐变到结束颜色。
在可视化中颜色映射可以突出数据的规律，较浅的颜色来显示较小的值，并使用较深的颜色显示较大的值。

我们只需在 `scatter()` 函数中的一个参数，就可将图形改变为颜色映射。

```python
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
    edgecolor='none', s=1)
```

![图7](C:\Users\wohez\Desktop\Python\matplotlib\7.jpg)

为了避免我们在作图之后忘记保存，我们可以在程序中直接添加自动保存功能。将 `show()` 函数替换为 `savefig()`

```python
plt.savefig('squares_plot.png', bbox_inches='tight')
```

---

---





### 绘制随机漫步图

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

---

---



### 使用 Pygal 来模拟抛骰子

#### 什么是 Pygal ？

> Pygal 是 Python 的可视化包，用来生成可缩放的矢量图形文件。对于需要在尺寸不同的屏幕上显示的图表，使用 Pygal 绘制将很有用，
> 因为他们可以进行自动的缩放。

#### 模拟骰子

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

#### 同时抛两个骰子

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

---

接下来，我们可以对代码进行重构，让他更具有可用性。

我们可以先更改 `x_label` 的设置，让设置更加自动化。

```python
for num in range(2, max_result + 1):
    x_labels.append(str(num))
hist.x_labels = x_labels.copy()
```

然后把 `die_visual.py` 文件重构为函数。

```python
def throw_two_dice(die_1_sides=6, die_2_sides=6):
    die_1 = Die(die_1_sides)
    die_2 = Die(die_2_sides)

# 抛几次骰子，并将结果存储在一个列表中
    results = []
    for roll_num in range(50000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

# 分析结果
    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(2, max_result + 1):
        frequency = results.count(value)
        frequencies.append(frequency)

    hist = pygal.Bar()

    hist.title = 'Results of rolling a D' + str(die_1.num_sides) + ' and a D' + str(die_2.num_sides) + ' dice 50,000 times.'
    x_labels = []
    for num in range(2, max_result + 1):
        x_labels.append(str(num))
    hist.x_labels = x_labels.copy()
    hist.x_title = 'Result'
    hist.y_title = 'Frequency of Result'

    hist.add('D' + str(die_1.num_sides) + '+ D' + str(die_2.num_sides), frequencies)
    hist.render_to_file('die_visual.svg')
```

---

---



### 使用 Python 处理以 CSV 个数存储的数据

#### 什么是 CSV ？

> **CSV**, Comma-Separated Values 是 逗号分隔值，其文件以纯文本存储表格数据（数字和文本）。
> CSV文件由任意数目的记录组成，记录间以某种换行符分隔；
> 每条记录由字段组成，字段间的分隔符是其它字符或字符串，最常见的是逗号或制表符。
> CSV是一种通用的广泛应用。最广泛的应用是在程序之间转移表格数据、相对简单的文件格式，被用户、商业和科学。

#### CSV 文件格式

```python
import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
```

在模块 `csv` 中存在一个阅读器类 `reader` ，我们创建一个读取 `filename` 的对象存储在 `reader` 中。
`reader` 类中的方法 `next()` 可以返回文件的下一行，而第一次调用就代表返回文件的第一行。我们将返回的数据存储在 `header_row` 中，
包含与天气相关的文件头，指出每行都包含哪些数据。

运行代码可得到

> ['AKDT', 'Max TemperatureF', 'Mean TemperatureF', 'Min TemperatureF', ...]

`reader` 处理文件以逗号分割第一行数据，并将每项数据都作为一个元素存储在列表中。

也可以更换另一种输出方式

```python
    for index, column_header in enumerate(header_row):
        print(index, column_header)
```

对列表调用 `enumerate()` 来获取每个元素的索引及其值。

> 0 AKDT
>
> 1 Max TemperatureF
>
> 2 Mean TemperatureF
>
> 3 Min TemperatureF
>
> ...

接下来可以分别处理第0行的日期和第1行最高气温

首先读取每天的最高气温：

```python
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
```

阅读器对象从其停留的地方继续向下读取 CSV 文件， 每次都是自动返回当前所处位置的下一行。
即从第二行开始读。

得到数据：

> ['64', '71', '64', '59', '69', '62', '61', ...]

之后对这些最高温度值绘制气温图表

```python
    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(highs, c='red')

    # 设置图形的格式
    plt.title("Daily high temperatures, July 2014", fontsize=24)
    plt.xlabel('',fontsize=16)
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
```

使用 `plot()` 函数绘画一个简单的折线图，
但是对 `xlabel()` 函数，由于还没有添加日期所以没有给x轴添加坐标。

接下来我们从文件中读取日期。从CSV文件中读取数据时获得的是一个字符串，
所以我们需要把字符串转化为一个表示相应日期的对象。

```python
dates = []
for row in reader:
    current_date = datetime.strptime(row[0], "%Y-%m-%d")
    dates.append(current_date)

plt.plot(dates, highs, c='red')
```

我们利用模块 `datetime` 中的函数 `strptime()` 来将日期数据转换为 `datetime` 类。
再调用 `autofmt_xdate()` 函数来绘制斜着的日期标签，以免他们彼此重叠。

```python
fig.autofmt_xdate()
```

绘制出图形：

![图1](C:\Users\wohez\Documents\GitHub\LearningProject_Python_Spring_2020\data\CSV\1.jpg)

修改读取文件，实现读取更大范围的数据。

![图2](C:\Users\wohez\Documents\GitHub\LearningProject_Python_Spring_2020\data\CSV\2.jpg)

再在图表中添加最低气温数据，使图表完整

```python
lows = []
for row in reader:
    low = int(row[3])
    lows.append(low)

plt.plot(dates, lows, c='blue')
```

![图3](C:\Users\wohez\Documents\GitHub\LearningProject_Python_Spring_2020\data\CSV\3.jpg)

可以使用函数 `fill_between()` 来将最高气温和最低气温之间的区域涂色，使得气温范围变得更加明显。

```python
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# alpha 代表透明度，从0~1逐渐透明
```

![图4](C:\Users\wohez\Documents\GitHub\LearningProject_Python_Spring_2020\data\CSV\4.jpg)

有时候我们获取的数据并不是完全正确的，可能原始数据中就会有一些错误。
如果按照上述程序来运行，若遇到存在错误的原始程序，则会导致程序崩溃，所以我们需要修改代码，使代码能够应对这个问题。

```python
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
```

每次我们从文件中提取信息，只要中间有一项确实，Python都会引发 ValueError 的异常
如果出现数据缺失，则会打印：

> 日期 + missing data





### 处理 JSON 文件存储的数据

#### 什么是 JSON 文件 ？

> JSON (javascript Object Notation) 格式最初是为了 JavaScript 开发的，
> 但随后成了一种常见格式，被包含 Python 在内的众多语言中。

模块 `json` 让你能够将简单的Python数据结构转储到文件中，
并在程序再次运行时加载该文件中的数据，你还可以使用 `json` 在 Python 程序之间分享数据。更重要的是，
JSON 数据格式并非 Python 专用的，这让你能够以 JSON 格式存储的数据与使用其他编程语言的人分享。

#### 下载收盘价数据

我们可以先从网上下载文件，在程序中对下载后的本地文件进行处理。
也可以从在程序运行的过程中直接通过程序读取网上的文档并处理。

方法一：先从网上下载文件，再在程序中读取本地文件

```python
import json
filename = 'btc_close_2017.json'
with open(filename) as f:
    file = json.load(f)

print(file)
```

方法二：直接在程序中从网上下载文件

1.使用模块 `urllib` 模块中的函数 `urlopen()` 将 url 传入到函数中，
Python 就会向网站发送请求，服务器响应后就把文件发送给 Python 

```python
from urllib.request import urlopen
import json

json_url = 'http://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
response = urlopen(json_url)
# 读取数据
req = response.read()
# 将数据写入文件
with open('btc_close_2017_urllib.json','wb') as f:
    f.write(req)
# 加载 json 格式
# 此时 req 和 f 可以互换
file_urllib = json.loads(req)
print(file_urllib)
```

2.使用模块 `requests` 中的方法，可以让上述过程变得简单
函数 `requests.get()` 可以从网络上下载文件到 Python 中的 `req` ，
`req.text` 为文件中的内容，而 `req.json()` 函数把内容转化为 Python 能够处理的格式。

```python
import requests

json_url = 'http://raw.githubsercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)
# 将数据写入文件
with open('btc_close_2017_request.json','w') as f:
    f.write(req.text)
file_requests = req.json()
```

#### 提取相关数据

为了方便使用 Pygal 作图，我们需要把文件中的数据提取到 Python 中，
并把数字字符串转化为 int 的格式方便处理。

```python
# 打印每一天的信息
for btc_dict in btc_data:
    date = btc_dict['date']
    month = int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    close = int(float(btc_dict['close']))
    print("{} is month {} week {}, {}, the close prise is {} RMB".format(date, month, week, weekday, close))
```

这里需要注意的是，`btc_dict['close']` 中的字符串为 '3928.6492' 形式的，
若直接转化为 int 格式，则会出现 `ValueError` 异常。
所以我们需要先 `float()` 转化为 float 类型，再 `int()`

> 得到的数据：
>
> 2017-01-01 is month 1 week 52, Sunday, the close prise is 6928 RMB
>
> 2017-01-02 is month 1 week 1, Monday, the close prise is 7070 RMB
>
> ......

#### 绘制收盘价折线图

在绘制折线图之前，我们需要首先获取 x 轴和 y 轴的信息，所以创建几个列表来存储数据。

```python
# 创建5个列表，分别存储日期和收盘价
dates, moenths, weeks, weekdays, close = [], [], [], [], []

# 每一天的信息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    moenths.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
```

我们使用 `pygal` 模块中的 `Line()` 函数，之后传入 x 轴和 y 轴参数，对图像的其他设置进行调整。

```python
import pygal
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价 (￥)'
line_chart.x_labels = dates
# x轴坐标每间隔20天显示一次
N = 20
line_chart.x_labels_major= dates[::N]
line_chart.add('收盘价', close)
line_chart.render_to_file('收盘价折线图(￥).svg')
```

显示的结果如下图：

![图1](C:\Users\wohez\Documents\GitHub\LearningProject_Python_Spring_2020\data\JSON\1.jpg)

#### 探索时间序列特征

> 进行时间序列分析，总是期望发现趋势，周期性，和噪声，从而能够根据事实，预测未来，做出决策。为了寻找周期性，需要首先将非线性的趋势消除。
> **对数变换**，是常用的处理方法之一。

从收盘价的折线图可以看出，2017年的总体趋势是非线性的，而且增长幅度不断增大，
似乎呈指数分布，但是我们还可以发现在每个嫉妒末似乎有一些相似的波动。尽管这些波动被增长的趋势掩盖了，
不过其中也许存在周期性。

使用 Python 标准库中的 `math` 模块，来对数据进行对数变换。

只对收盘价进行对数变换，而不改变日期叫做半对数变换。

```python
close_log = [math.log10(num) for num in close]
line_chart.add('收盘价', close_log)
line_chart.render_to_file('收盘价对数折线图(￥).svg')
```

用对数变换剔除非线性趋势之后，整体上涨的趋势更接近线性增长。并可以大致从图中看出周期性。三月，六月，九月，都出现了明显的波动。

![图2](C:\Users\wohez\Documents\GitHub\LearningProject_Python_Spring_2020\data\JSON\2.jpg)





### 使用API

#### 什么是 API ?

> Web API 是网站的一部分，用于与使用非常具体的 URL 请求特定信息的程序交互。
> 这种请求称为 API 调用。
> 请求的数据将以易于处理的格式（如JSON或CSV）返回。依赖于外部数据源的大多数应用程序都依赖于 API 调用，如
> 继承社交媒体网站的应用程序。

我们将以 Github 网站为例，了解 API 的使用。

Github 的API可以让我们能够通过API调用来请求各种信息。在浏览器输入：

```html
https://api.github.com/search/repositories?q=language:python&sort=stars

/*
api.github.com/ 将请求发送到 Github 网站中响应 API 调用的部分;
search/repositories 让 API 搜索 Github 上的所有代码库
? 代表我们要传入一个实参
q 代表查询，= 代表开始查询
language:python 代表我们只想获取语言为 python 的代码库
&sort=stars 代表排序的顺序是按照星数排序
*/
```

得到的结果如下：

    {
    "total_count": 4812373,
    "incomplete_results": false,
    "items": [
      {
        "id": 83222441,
        "node_id": "MDEwOlJlcG9zaXRvcnk4MzIyMjQ0MQ==",
        "name": "system-design-primer",
        -snip--

可以看出，响应的结果是一个字典，包含了三个 key ，分别是 `total_count` 库总数,`incomplete_results` 未完成结果,`items` 成员

#### 处理 API 响应 

接下来我们编写程序，处理 API 响应。

```python
import requests

# 执行API调用并存储相应
url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()

# 处理结果
print(response_dict.keys())
```

使用模块 `requests` 来执行调用，调用函数 `get()` 将响应对象存储在变量 `r`， 对象中存在一个属性 `status_code`，他是一种状态码，
让我们判断请求是否成功。状态码200表示请求成功。

再调用 `json()` 函数将 API 返回的信息转化为 Python 能够处理的字典格式。
将字典存储在 `response_dict` 中。输出字典中的键得到：

> Status code: 200
>
> dict_keys(['total_count', 'incomplete_results', 'items']) 

#### 处理响应字典

得到 API 字典之后，就可以处理这个字典中的数据

```python
# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))

# 研究第一个仓库
repo_dict = repo_dicts[0]
print("\nKeys: ", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
```

与 `items` 相关联的值是一个列表，其中包含很多字典，每个字典都包含有关一个 Python 仓库的信息。
而对于每一个仓库字典，包含了这个库的许多信息。我们可以通过打印一个仓库字典中的键得到仓库的一些信息。

运行结果：

```
Keys:  74
archive_url
archived
assignees_url
--snip--
url
watchers
watchers_count
```

Github 的 API 返回有关仓库的大量信息，从返回结果看有 74 个键，
我们通过查看这些键就可以了解仓库的大致信息。

#### 输出最受欢迎的仓库

接下来借助代码来查看这些信息。在循环中我们打印每个项目的名称，所有者，星级，在 Github 上的 URL 及其描述。

```python
for repo_dict in repo_dicts:
    print("\nSelected information about first repository:")
    print("Name: ", repo_dict['name'])
    print("Owner: ", repo_dict['owner']['login'])
    print("Star: ", repo_dict['stargazers_count'])
    print("Repository: ", repo_dict['html_url'])
    print("Created: ", repo_dict['created_at'])
    print("Updated: ", repo_dict['updated_at'])
    print("Description: ", repo_dict['description'])
```

得到的结果

```
Selected information about first repository:
Name:  awesome-python
Owner:  vinta
Star:  79188
Repository:  https://github.com/vinta/awesome-python
Created:  2014-06-27T21:00:06Z
Updated:  2020-02-13T06:49:04Z
Description:  A curated list of awesome Python frameworks, libraries, software and resources

Selected information about first repository:
Name:  public-apis
Owner:  public-apis
Star:  70563
Repository:  https://github.com/public-apis/public-apis
Created:  2016-03-20T23:49:42Z
Updated:  2020-02-13T07:01:48Z
Description:  A collective list of free APIs for use in software and web development.

--snip--

Selected information about first repository:
Name:  localstack
Owner:  localstack
Star:  23017
Repository:  https://github.com/localstack/localstack
Created:  2016-10-25T23:48:03Z
Updated:  2020-02-13T06:51:02Z
Description:  💻  A fully functional local AWS cloud stack. Develop and test your cloud & Serverless apps offline!
```

#### 使用 Pygal 可视化仓库

使用 `Pygal` 模块中的函数 `Bar()` 构建柱状图

```python
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 探索有关仓库的信息
repo_dicts = response_dict['items']

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Project on Github'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')
```

显示的柱状图：
![图1](C:\Users\wohez\Documents\GitHub\LearningProject_Python_Spring_2020\data\API\1.jpg)

接下来来改进这个图表，进行多方面的定制。

```python
# 可视化
my_style = LS('#333366', base_style=LCS)

# 创建 Config 对象
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
# 设置标题标签的字体大小
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
# 缩短较长的字符为15个
my_config.truncate_label = 15
# 隐藏水平线
my_config.show_y_guides = False
# 自定义宽度
my_config.width = 1000

chart = pygal.Bar(config=my_config, style=my_style)
```

得到的图像：

![图2](C:\Users\wohez\Documents\GitHub\LearningProject_Python_Spring_2020\data\API\2.jpg)

为了让图表中显示更多的信息，而不仅仅是代码库的名字和star数。我们可以创建一个列表存放我们想要添加的信息。

```python
plot_dicts = []

plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

--snip--

chart.add('', plot_dicts)
```

这样我们就可以得到既包含星数还包含代码库的描述以及网址，并实现点击表格就可以跳转到该网址。

![图3](C:\Users\wohez\Documents\GitHub\LearningProject_Python_Spring_2020\data\API\3.jpg)