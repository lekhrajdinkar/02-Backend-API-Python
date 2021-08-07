import datetime

dt = datetime.datetime


def format_datetime(dt1: datetime):
    """
    print date time seperately with no miliisecond info
    :param dt1: datetime to be print
    """
    dt = str(dt1).split(" ")
    print('date : {}\ntime : {}'.format(dt[0], dt[1]).split('.')[0])
    return dt


format_datetime(dt.utcnow())

print(dt.now(), dt.today(), dt.utcnow(), sep='\n')
