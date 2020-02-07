

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




