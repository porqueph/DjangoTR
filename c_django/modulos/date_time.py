from datetime import datetime
import calendar



date = datetime(2023,4,8, 7, 49, 23)

print(date)

data_str_data = '2022-04-20 07:49:23'

data_str_fmt = '%Y-%m-%d %H:%M:%S'

data = datetime.strptime(data_str_data, data_str_fmt)
print(data)


print(calendar.calendar(2023))