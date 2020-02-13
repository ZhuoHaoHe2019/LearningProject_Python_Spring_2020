from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from urllib.request import urlopen
import json
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

# 创建5个列表，分别存储日期和收盘价
dates, months, weeks, weekdays, close = [], [], [], [], []

# 每一天的信息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

import pygal
import math

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价 (￥)'
line_chart.x_labels = dates
# x轴坐标每间隔20天显示一次
N = 20
line_chart.x_labels_major= dates[::N]
for num in close:
    close_log = [math.log10(num)]
line_chart.add('收盘价', close_log)
line_chart.render_to_file('收盘价对数折线图(￥).svg')

