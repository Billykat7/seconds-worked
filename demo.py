import worked as worked_lib


start_time = input('Enter Start Time(08:00:00): ')
end_time   = input('Enter End Time(17:00:00): ')
date       = input('Date of Operation(01.01.2022): ')

TIME_SEC = worked_lib.CalculateTime(start_time, end_time, dat=date)

worked_time = TIME_SEC.time_in_seconds()
print(worked_time)
