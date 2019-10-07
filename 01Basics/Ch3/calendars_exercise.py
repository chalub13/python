#
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.MONDAY)
st = c.formatmonth(2017, 1, 0, 0)
print(st)

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.MONDAY)
st = hc.formatmonth(2017, 1)
print(st)


# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2017, 1):
    print(i)

# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
print("Months")
for name in calendar.month_abbr:
    print(name)

print("Days:")
for day in calendar.day_abbr:
    print(day)

# Calculate days based on a rule: For example, consider
# a team meeting     on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print()
for m in range(1, 13):
    c = calendar.TextCalendar(calendar.SUNDAY)
    print(c.formatmonth(2019, m, 0, 0))
    cal = calendar.monthcalendar(2019, m)
    print(cal)
    weekone = cal[0]
    weektwo = cal[1]

    print(weekone)
    print(weektwo)

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))
