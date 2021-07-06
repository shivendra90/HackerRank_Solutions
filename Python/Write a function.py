def is_leap(year):
    while 1900 <= year <= 10**5:
        return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
