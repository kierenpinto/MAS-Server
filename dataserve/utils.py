import time, datetime
def date_range(mindate, maxdate):
    maxdateobj = datetime.datetime(mindate['year'],mindate['month'],mindate['day'],hour=mindate['hour'],minute=mindate['min'],second=mindate['sec'],microsecond=0, tzinfo=None,fold=0)
    mintuple = maxdateobj.timetuple()
    min_epoc_sec = time.mktime(mintuple)
    mindateobj = datetime.datetime(maxdate['year'],maxdate['month'],maxdate['day'],hour=maxdate['hour'],minute=maxdate['min'],second=maxdate['sec'],microsecond=0, tzinfo=None,fold=0)
    maxtuple = mindateobj.timetuple()
    max_epoc_sec = time.mktime(maxtuple)
    return [min_epoc_sec, max_epoc_sec]