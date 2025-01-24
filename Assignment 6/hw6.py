"""
Write a function called get_decimal_time() that will accept three integer parameters,
each representing a conventional hour, minute, and second, respectively. You can assume
that this function will always receive positive arguments during invocation. It will
then use this information to determine its decimal equivalent, which it will return in
a "HOUR:MIN:SEC" format. Recall that French revolutionary days each have 10 hours, each
with 100 minutes, each with 100 seconds.

"""

def get_decimal_time(hour, minute, second):

    total_sec = (hour * 3600) + (minute * 60) + second

    new_hour = total_sec // 10000
    new_min = (total_sec % 10000) // 100
    new_sec = total_sec % 100

    return f'{new_hour}:{new_min}:{new_sec}'

"""
Write a function called get_decimal_date() that will accept three integer parameters, 
each representing a Gregorian month number (i.e. 1 through 12 ), a date of the month 
(assume 1 through 30 ), and a Common Era year, respectively. Your function will then 
use this information to convert this date to its French revolutionary equivalent, and 
return it as a string of "[Day] [month] [year], Décade [décade]". Since months in this 
system have only three 10-day weeks, you can easily figure out the décade by checking 
in which of the weeks the current date is. Finally, the revolutionary year is the 
difference between the Gregorian year and 1792 , the year the calendar was implemented.

"""
def get_decimal_date(greg_month, date, greg_year):

    if greg_month == 1:
        rev_month = 'Nivôse'
    elif greg_month == 2:
        rev_month = 'Pluviôse'
    elif greg_month == 3:
        rev_month = 'Ventôse'
    elif greg_month == 4:
        rev_month = 'Germinal'
    elif greg_month == 5:
        rev_month = 'Floréal'
    elif greg_month == 6:
        rev_month = 'Prairial'
    elif greg_month == 7:
        rev_month = 'Messidor'
    elif greg_month == 8:
        rev_month = 'Thermidor'
    elif greg_month == 9:
        rev_month = 'Fructidor'
    elif greg_month == 10:
        rev_month = 'Vendémiaire'
    elif greg_month == 11:
        rev_month = 'Brumaire'
    else:
        rev_month = 'Frimaire'

    rev_year = greg_year - 1792

    if 1 <= date <= 10:
        decade = 1
    elif 10 < date <= 20:
        decade = 2
    else:
        decade = 3

    return f'{date} {rev_month} Year {rev_year}, Décade {decade}'

"""
Your last function will be called get_french_datetime() , and it will accept a single 
string parameter containing a Gregorian date and time. Your function must then isolate 
each piece of information from this string, and pass the relevant information to 
get_decimal_time() and get_decimal_date() to get their respective decimal equivalent. 
Your function must return a string with two lines: the first giving you the decimal time, 
and the second giving you the decimal date. Note that you may not assume that the location 
of the : characters will always be the same. 

"""
def get_french_datetime(greg_datetime):

    colon = int(greg_datetime.find(':'))
    colon_two = int(greg_datetime.find(':', greg_datetime.find(':') + 1))
    space = int(greg_datetime.find(' '))
    slash = int(greg_datetime.find('/'))
    slash_two = int(greg_datetime.find('/', greg_datetime.find('/') + 1))

    hour = greg_datetime[:colon]
    minute = greg_datetime[colon + 1:colon_two]
    second = greg_datetime[colon_two + 1:space]

    greg_month = greg_datetime[space + 1:slash]
    date = greg_datetime[slash + 1:slash_two]
    greg_year = greg_datetime[slash_two + 1:]

    time = get_decimal_time(int(hour), int(minute), int(second))
    date = get_decimal_date(int(greg_month), int(date), int(greg_year))

    return f'{time}\n{date}'


def main():
    decimal_time = get_decimal_time(16, 7, 46)
    print(decimal_time)

    revolutionary_date = get_decimal_date(3, 22, 2022)
    print(revolutionary_date)

    greg_datetime = '16:07:46 03/22/2022'
    french_datetime = get_french_datetime(greg_datetime)
    print(french_datetime)


main()
