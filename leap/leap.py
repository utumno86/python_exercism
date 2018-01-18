"""The module also returns whether or not a given year is a leap year"""
def is_leap_year(year):
    """returns whether or not a given year is a leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
