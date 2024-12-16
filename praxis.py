import calendar
from datetime import datetime

# tagesansicht
def show_day(year, month, day):
    try:
        #wochentag ermitteln
        weekday_index = datetime(year, month, day).weekday()
        weekday_name = calendar.day_name[weekday_index]
        

        print(f"\nTagesansicht: {day:02}.{month:02}.{year}")
        print(f"Wochentag: {weekday_name}")

        #Termine
        print("Keine Termine vorhanden.")
    except ValueError:
        print("Ungültiges Datum!")    

year = 2024
month = 12
today = datetime.now()

#monat
month_calendar = calendar.monthcalendar(year, month)

print(f"{calendar.month_name[month]} {year}".center(20))
print("Mo Di Mi Do Fr Sa So")


for week in month_calendar:
    for day_index, day in enumerate(week):
        if day == 0:  # Leere Tage
            print("  ", end=" ")
        elif day == today.day and month == today.month and year == today.year:
            # Heutiges Datum markieren
            print(f"\033[92m{day:2}\033[0m", end=" ")  # Grün markieren
        elif day_index >= 5:  # Wochenende
            print(f"\033[91m{day:2}\033[0m", end=" ")  # Rot markieren
        else:
            print(f"{day:2}", end=" ")
    print()            
            

heute = datetime.now()
print(f"Heute ist: {heute.day:02}.{heute.month:02}.{heute.year}")         #ausgabe heutiges datum    
