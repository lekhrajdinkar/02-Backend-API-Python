import pytz, datetime as dt

def swapDict(d : dict):
    d_new ={}
    for k in d:
        d_new.setdefault(d[k], k)
    return d_new


def printAllTzList0():
    for tz in pytz.all_timezones: print(tz)

def findCountryCodebyPattern(pattern: str) -> list:
    result = set()
    for tzc in pytz.country_timezones: #dict
        for z in pytz.country_timezones[tzc]: #list
            if pattern in z:
                result.add(tzc)
    #print(result)
    return result

def getCountryName(code):
    if code in pytz.country_names: return pytz.country_names[code]

def getAllCountryName() -> list:
    result = list()
    for code in pytz.country_names:
        print(code.center(30), pytz.country_names[code] )
        result.append(code.center(30) + pytz.country_names[code] )
    return result

def findtzbyCountryCode(code: str) -> list:
    if code in pytz.country_names.keys():
        print(code, getCountryName(code).center(30), pytz.country_timezones.get(code, None),  sep=': ')
        if pytz.country_timezones.get(code, None):
            printdatetimeAlongWithUTC(pytz.country_timezones.get(code))
    else: print(f'Time zone not found for country code :: {code}')

def findAlltz() -> list:
    #for t in pytz.all_timezones:
    for code in pytz.country_names.keys():
        print(code, getCountryName(code).center(30), pytz.country_timezones.get(code, ' === NO TZ ==='), sep=': ')

def printdatetimeAlongWithUTC(country_tz_name_list):
    print('country_tz_name_list >>', country_tz_name_list)
    for country_tz_name in country_tz_name_list:
        country_tz = pytz.timezone(country_tz_name)
        result = dt.datetime.now(tz=country_tz)
        print(country_tz_name.center(40), result, sep=': ')
        utc_dt = dt.datetime.utcnow()
        print('UTC'.center(40), utc_dt, sep=': ',end='\n'+('=*=*='*15)+'\n')


# PRG-1
# findtzbyPattern('Asia/K')
def search():
    pattern = input('Search :: Enter pattern to find country code or timeZone name >> ')
    result = findCountryCodebyPattern(pattern)
    if len(result) == 0:
        d = swapDict(pytz.country_names)
        for k in d:
            if pattern in k:
                result.append(d[k])
    if len(result) == 0:
        print('No Country code found !! try different pattern ')
    print('Found these Country codes :: ')
    print(*result , sep='\n\t', end='\n===== end prg-1 =====\n\n')

# prg-2
def prg2():
    while True:
        print('Menu \n0 - See All Country codes \n1 - See All TimeZones (Group by Country) \n2 - Search Country codes by pattern\ne - end\n', end='^'*50 )
        code = input('\nEnter country code, to see datetime with country specific timezone ::  >> ')
        if code == '0': getAllCountryName()
        elif code == '1': findAlltz()
        elif code == '2': search()
        elif code == 'e': break
        else: findtzbyCountryCode(code)


# Execution
#prg1()
print(getAllCountryName())
print(swapDict(pytz.country_names))
prg2()


