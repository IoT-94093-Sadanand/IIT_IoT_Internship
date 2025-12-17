import datetime as d

#cd=d.date(1982,8,23)

cd=d.datetime.now()
print(d.datetime.now())

day=cd.strftime("%A")
print(day)
