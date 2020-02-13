

#### 什么是 *matplotlib* ？

***

*matplotlib* 是一个数学绘图库， 我们可以用它来制作一些简单的图表，例如折线图，或散点图。



#### 绘制简单的折线图

---

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

#### 绘制简单的散点图

---

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

![图4](C:\Users\wohez\Desktop\Python\matplotlib\4.jpg)

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
