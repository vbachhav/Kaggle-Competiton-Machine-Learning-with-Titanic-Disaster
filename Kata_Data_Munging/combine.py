#importing regex library to validate the records in data file
import re

#defining custom regex patterns for football and weather data file
football_regex = re.compile(r'\s+\d+\. (?P<Team>\w+).*?(?P<F>\d+)\s+-\s+(?P<A>\d+).*')
weather_regex = re.compile(r'^\s+(?P<day>\d+)\s+(?P<max>\d+)\s+(?P<min>\d+).*')

#object oriented classs to compute the min and max difference
class solution(object):
    def __init__(self, regex, file_name):
        self.regex = regex
        self.file_name = file_name

    def compute(self, func):
        result_dict = {}
        for line in open(self.file_name):
            valid_line = self.regex.match(line)
            if valid_line:
                result_dict[valid_line.group(1)] = int(valid_line.group(2)) - int(valid_line.group(3))

        return func(result_dict, key=lambda x: result_dict[x])

print 'Day having lowest difference in max and min temperature is: ',solution(weather_regex, 'weather.dat').compute(min)
print 'Team having lowest goal difference at end of season is: ',solution(football_regex, 'football.txt').compute(min)