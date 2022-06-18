#Laboratorio 4.3.1.8
#Elaborado por: Ariadna Loredo

def is_year_leap(year):
    if year % 4 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 400 == 0:
        return True

def days_in_month(year, month):
    months=[30,28,31,30,31,30,31,31,30,31,30,31]
    if is_year_leap(year) and month == 2:
        return months[month-1] +1
    if not is_year_leap(year) and month == 2:
        return months[month-1]
    if month in range(1,13):
        return months[month-1]
    else:
        return None

#def day_of_year(year, month, day):
#    dias = 0
#    for d in range(1, month):
        
#print(day_of_year(2000, 12, 31))