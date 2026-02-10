from datetime import date
from calendar import TextCalendar

today = date.today()

text_calendar = TextCalendar()  # create a text calendar object
print(text_calendar.formatmonth(1752, 9))  # format one month as text

