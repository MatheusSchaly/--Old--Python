import datetime
import pytz

print("Choose a time zone:")

for i in range(361, 370):
    print(pytz.all_timezones[i])

tz = input()
tz_to_display = pytz.timezone(tz)

print("The time in {} is {} / {}".format(tz,
                                       datetime.datetime.now(tz=tz_to_display).strftime("%A %x %X %z"),
                                       datetime.datetime.now(tz=tz_to_display).tzname()))
print("Now: ", datetime.datetime.now().strftime("%A %x %X"))
print("UTC: ", datetime.datetime.utcnow().strftime("%A %x %X"))
