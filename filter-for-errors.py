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

# common function to take care of all error types
def error_type_count()
