from datetime import date, timedelta
from calendar import monthrange


def meetup_day(year, month, weekday, position):
    number_of_days = monthrange(year, month)[1]
    meta_start_date = date(year, month, 1)
    start_date = date(year, month, calculate_start_date(meta_start_date, weekday))
    day = calculate_day(position, start_date, number_of_days)
    if day.month != month:
        raise MeetupDayException('Your parameters specify a day that does not exist')
    else:
        return date(year, month, day.day)


def calculate_day(position, start_date, number_of_days):
    positon_key = {
        '1st': 1,
        '2nd': 2,
        '3rd': 3,
        '4th': 4,
        '5th': 5,
        'first': 1
    }
    if position == 'teenth':
        while start_date.day < 13:
            start_date += timedelta(days=7)
    elif position == 'last':
        while start_date.day < number_of_days - 6:
            start_date += timedelta(days=7)
<<<<<<< HEAD

=======
>>>>>>> 371894dab186cec701ce325dcc4d002c02d93cbd
    else:
        start_date += timedelta(days=(7 * (positon_key[position] - 1)))
    return start_date


def calculate_start_date(meta_start_date, weekday):
    weekday_key = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6,
        }
    while meta_start_date.weekday() != weekday_key[weekday]:
        meta_start_date += timedelta(days=1)
<<<<<<< HEAD
    return meta_start_date.day
=======
    return meta_start_date.day
>>>>>>> 371894dab186cec701ce325dcc4d002c02d93cbd
