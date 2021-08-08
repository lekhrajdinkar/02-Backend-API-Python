import pytz
import datetime as dt

#tz present - aware, else naive

aware_time: dt = pytz.utc.localize(dt.datetime.now()).astimezone()
print(aware_time, aware_time.tzinfo, type(aware_time))

aware_time2: dt = dt.datetime.now(tz=pytz.timezone('Japan'))
print(aware_time2, aware_time2.tzinfo, type(aware_time2))

