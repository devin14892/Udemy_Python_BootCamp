emp_hours = [('Abby',100),('Billy',400),('Vassie',800),('Devin',700)]

#for ticker,prices in stock_prices:
#    print(ticker,prices)


def employee_month(employeename_hoursworked):

    employee_hours = 0
    employee_name = ''
    
    for person,hours in employeename_hoursworked:
        if hours > employee_hours:
            employee_name = person
            employee_hours = hours
        else:
            pass
    return (employee_name,employee_hours)

name,hours = employee_month(emp_hours)

print(name,'worked the most hours with',hours)



