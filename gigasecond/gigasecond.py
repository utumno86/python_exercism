from datetime import datetime
from datetime import timedelta


def add_gigasecond(time):
    gs = 10**9
    return time + timedelta(seconds=gs)
