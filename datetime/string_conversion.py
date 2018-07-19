import datetime

d = datetime.datetime(2016, 7, 30, 13, 30, 10, 00)

print(d)
print(d.ctime())
print(d.second)

# convert datetime to string
print(datetime.datetime.today().strftime("%Y-%m-%d"))
print(datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S"))

# convert string to date time
d = datetime.datetime.strptime("2016-05-08-12-12-00", "%Y-%m-%d-%H-%M-%S")

print(d)
