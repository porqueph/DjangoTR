from datetime import datetime




date = datetime(2023,4,8, 7, 49, 23)

print(date)

data_str = '2022-04-20 07:49:23'

data = datetime.strptime(data_str)