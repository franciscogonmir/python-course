isLeapYear = lambda year : year % 2 == 0
year = int(input("Enter year: "))
if isLeapYear(year):
    print(str(year) + " is leap year")
else:
    print(str(year) + " is not leap year")

