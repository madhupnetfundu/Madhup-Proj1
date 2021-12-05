import pygal
my_file = open('/Users/madsriva/Documents/Cases/ExxonMobil/controller-logs/server.log')
SEVERE_Count = 0
INFO_Count = 0
WARNING_Count = 0
## INFO ##
my_file.seek(0)
for line in my_file:
    if "INFO" in line:
        INFO_Count = INFO_Count + 1
    else:
        pass
print (INFO_Count)

## SEVERE ##
my_file.seek(0)
for line in my_file:
    if "SEVERE" in line:
        SEVERE_Count = SEVERE_Count + 1
    else:
        pass
print (SEVERE_Count)


## WARNING ##
my_file.seek(0)

for line in my_file:
    if "WARNING" in line:
        WARNING_Count = WARNING_Count + 1
    else:
        pass
print (WARNING_Count)


pie_chart=pygal.Pie()
pie_chart.title='Error Distribution as observed on server.log'
pie_chart.add('SEVERE', SEVERE_Count)
pie_chart.add('WARNING', WARNING_Count)
pie_chart.add('INFO', INFO_Count)
pie_chart.render_to_file('error-pie-chart.svg')