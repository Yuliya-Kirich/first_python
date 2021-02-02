seconds = input("Введите время в секундах  >>>>> ")
hour_date = int(seconds)//3600
minute_date = int(seconds) % 3600//60
seconds_date = int(seconds) % 3600 % 60

date = '{:02d}:{:02d}:{:02d}'.format(hour_date, minute_date, seconds_date)
print(date)
