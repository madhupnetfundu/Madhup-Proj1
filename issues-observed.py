def check_error_category(file,error-type):
    file-to-check = open(file)
    SEVERE = 0
    for line in file-to-check:
        if error-type in file-to-check:
            SEVERE = SEVERE + 1
        else:
            pass
    return count
    print (count)

check_error_category('/Users/madsriva/Documents/Cases/ExxonMobil/controller-logs/server.log','SEVERE')