import calendar
import datetime
import re

import holidays
from pydantic import BaseModel


sa_holidays    = holidays.ZA()
date_today     = datetime.datetime.now()
date_today_iso = datetime.datetime.now().isoformat()
holiday_check  = date_today in sa_holidays
weekday_check  = (calendar.day_name[date_today.weekday()]).upper()
print(f'The current time is: {date_today}\n')


class CalculateTime:
    """docstring for Main"""
    def __init__(self, start_time, end_time, **kwargs):
        super(CalculateTime, self).__init__()
        self.start_time = start_time
        self.end_time   = end_time
        self.date       = kwargs.get('date') if kwargs.get('date') else None
        
    def time_in_seconds(self):
        
        if weekday_check in ['SATURDAY', 'SUNDAY']:
            return {'error' : 'No calculations allowed on Weekends'}

        elif holiday_check == True:
            return {'error' : 'No calculations allowed on SA public holidays'}

        else:

            try:

                if self.start_time == None:
                    return {'error' : 'Waiting for time values to be entered....'}

                time_start_str = re.findall('[0-9]+', self.start_time)
                numbers_pulled = [int(time_cut_str) for time_cut_str in time_start_str]

                if numbers_pulled[0] > 24 or numbers_pulled[1] > 60 or numbers_pulled[2] > 60:
                    return {'error' : 'Hours must be less than 24, minutes less than 60 and Seconds less than 60'}
    
                self.start_time = (numbers_pulled[0]) * 3600 + (numbers_pulled[1]) * 60 + numbers_pulled[2]

                if self.start_time < 28800:
                    return {'error' : 'Date requested is a public holidays. Weekdays only, from 08:00 - 17:00'}

                elif 61200 < self.start_time:
                    return {'error' : 'Date requested is a public holidays. Weekdays only, from 08:00 - 17:00'}

                if self.end_time == None:
                    return {'error' : 'Waiting for time values to be entered....'}

                end_time_str  = re.findall('[0-9]+', self.end_time)
                number_pulled = [int(timeCutE) for timeCutE in end_time_str]

                if number_pulled[0] > 24 or number_pulled[1] > 60 or number_pulled[2] > 60:
                    return {'error' : 'Hours are less than 24, minutes less than 60 and Seconds less than 60'}

                end_time = (number_pulled[0]) * 3600 + (number_pulled[1]) * 60 + number_pulled[2]
    
                if end_time < 28800:
                    return {'error' : 'No public holidays. Weekdays only, from 08:00 - 17:00'}

                elif 61200 < end_time:
                    return {'error' : 'No public holidays. Weekdays only, from 08:00 - 17:00'}
    
                if end_time > self.start_time:
                    time_difference = int(end_time - self.start_time)

                else:
                    return {'error': 'The End time cannot be less than the Start time'}
    
                return {'worked_seconds': time_difference}

            except Exception as e:
                return {'error': 'There was an error ' + str(e)}
