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
>...

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