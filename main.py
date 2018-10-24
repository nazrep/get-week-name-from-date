import calendar

given_date = input("Podaj date, a otrzymasz dzień tygodnia :) (YYYY/MM/DD)")
year, month, day = given_date.split("/")
x = int(year)
y = int(month)
z = int(day)
index_of_dayweek = calendar.weekday(x, y, z)
days=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]


print(days[index_of_dayweek])
