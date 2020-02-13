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




