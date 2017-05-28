#importing regex library to validate the records in data file
import re

#defining custom regex patterns for football data file
weather_regex = re.compile(r'^\s+(?P<day>\d+)\s+(?P<max>\d+)\s+(?P<min>\d+).*')

#defination to calculate the difference between max and min temperatures
def weather():
    res = {}
    for line in open('weather.dat'):
        m = weather_regex.match(line)
        if m:
            res[m.group('day')] = int(m.group('max')) - int(m.group('min'))
    print 'Day having lowest difference in max and min temperature is: ', min(res, key=lambda x: res[x])#returning the key from dictionary having minimum temp difference value

weather()