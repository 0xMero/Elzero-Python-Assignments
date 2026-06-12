# Assignment 1
import datetime
# Date = datetime.datetime(2021, 6, 25)
# Today = datetime.datetime.now()
# print(f"Days From 2021-06-25 To {Today.date()} Is => {(Today - Date).days}")
# Assignment 2
Today = datetime.datetime(2021, 8, 10)
print(Today.date())
print(Today.date().strftime("%b %d, %Y"))
print(Today.date().strftime("%d - %b - %Y"))
print(Today.date().strftime("%d / %b / %y"))
print(Today.date().strftime("%a, %d %B %Y"))