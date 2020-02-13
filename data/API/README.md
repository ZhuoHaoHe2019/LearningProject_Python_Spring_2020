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
![图1](ZhuoHaoHe2019/LearningProject_Python_Spring_2020/data/API/1.jpg)

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

![图2](ZhuoHaoHe2019/LearningProject_Python_Spring_2020/data/API/2.jpg)

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

![图3](ZhuoHaoHe2019/LearningProject_Python_Spring_2020/data/API/3.jpg)
