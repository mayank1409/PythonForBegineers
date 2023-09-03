import datetime

print('Now ', datetime.datetime.today())
print('Now plus 90 Days ', datetime.datetime.today() + datetime.timedelta(days=90))
print('Now plus 3 weeks ', datetime.datetime.today() + datetime.timedelta(weeks=3))
print('Now plus 24 hours ', datetime.datetime.today() + datetime.timedelta(hours=24))

print('Year ', datetime.datetime.today().year)
print('Month ', datetime.datetime.today().month)
print('Day ', datetime.datetime.today().day)

print('Hour ', datetime.datetime.today().hour)
print('Minute ', datetime.datetime.today().minute)
print('Second ', datetime.datetime.today().second)

date_27_5_2019 = datetime.datetime(2019, 5, 27)
print(date_27_5_2019)

print('Time ', date_27_5_2019.time())

today = datetime.datetime.today()
print('Logging Today using str ', today.__str__())
print('Logging Today using repr ', today.__repr__())
