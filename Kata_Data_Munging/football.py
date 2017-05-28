#importing regex library to validate the records in data file
import re

#defining custom regex patterns for football data file
football_regex = re.compile(r'\s+\d+\. (?P<Team>\w+).*?(?P<F>\d+)\s+-\s+(?P<A>\d+).*')

#defination to calculate the goal difference
def football():
    res = {}
    for line in open('football.txt'):
        m = football_regex.match(line)
        if m:
            res[m.group('Team')] = int(m.group('F')) - int(m.group('A'))
    print 'Team having lowest goal difference at end of season is: ', min(res, key=lambda x: res[x]) #returning the key from dictionary having minimum goal difference value

football()
