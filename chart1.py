import pygal
pie_chart=pygal.Pie()
pie_chart.title='Some Browsers'
pie_chart.add('IE', 19.5)
pie_chart.add('Firefox', 36.6)
pie_chart.add('Chrome', 36.3)
pie_chart.add('Safari', 4.5)
pie_chart.add('Opera', 2.3)
pie_chart.render_to_file('progs-pie-chart.svg')