uDay = int(input("Insert an amount of days: "))
uHours = int(input("Insert an amount of hours: "))
uMinutes = int(input("Insert an amount of minutes: "))
uSeconds = int(input("Insert an amount of seconds: "))

secDay = (uDay * 24) * 3600  
secMin = uMinutes * 60
secHrs = uHours * 3600

totalSeconds = secDay + secHrs + secMin
print totalSeconds


