from die import Die
import pygal
#
# # 创建两个D6（六面骰子）
# die_1 = Die()
# die_2 = Die(10)
#
# # 抛几次骰子，并将结果存储在一个列表中
# results = []
# for roll_num in range(50000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)
#
# # 分析结果
# frequencies = []
# max_result = die_1.num_sides + die_2.num_sides
# for value in range(2, max_result + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
#
# hist = pygal.Bar()
#
# hist.title = 'Results of rolling a D6 and a D10 dice 50,000 times.'
# x_labels = []
# for num in range(2, max_result + 1):
#     x_labels.append(str(num))
# hist.x_labels = x_labels.copy()
# hist.x_title = 'Result'
# hist.y_title = 'Frequency of Result'
#
# hist.add('D6 + D10', frequencies)
# hist.render_to_file('die_visual.svg')

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

throw_two_dice(6, 9)