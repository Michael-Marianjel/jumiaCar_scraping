from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days = 1)

# yesterday = today - datetime.timedelta(days=1)
# day_month = str(date.today()).split("-")
# date = day_month[2] + "/" + day_month[1]

print(yesterday)


