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


def get_user_input():
    day = int(input("Gib den Tag ein: "))
    month = int(input("Gib den Monat ein: "))
    year = int(input("Gib das Jahr ein: "))
    return year, month, day


# Tagesansicht mit input
def show_day(year, month, day):
    try:
        weekday_index = datetime(year, month, day).weekday()
        weekday_name = calendar.day_name[weekday_index]
        print(f"\Tagesansicht: {day:02}.{month:02}.{year}")
        print(f"Wochentag: {weekday_name}")

        print("Keine Termine vorhanden.")
    except ValueError:
        print("Ungültiges Datum!")


year, month, day = get_user_input()
show_day(year, month, day)


def show_week(year, month, day):
    try:
        # Startdatum der Woche ermitteln
        selected_date = datetime(year, month, day)
        start_of_week = selected_date - timedelta(days=selected_date.weekday())

        print(f"\nWochenansicht für die Woche von {start_of_week.strftime('%d.%m.%Y')}:")

        # Alle 7 Tage der Woche anzeigen
        for i in range(7):
            current_day = start_of_week + timedelta(days=i)
            weekday_name = calendar.day_name[current_day.weekday()]
            print(f"{weekday_name}: {current_day.strftime('%d.%m.%Y')}")
            # Hier können später Termine angezeigt werden
            print("  Keine Termine vorhanden.")
    except ValueError:
        print("Ungültiges Datum!")



# Beispiel-Dictionary, um Termine zu speichern:
appointments = {
    "1996-02-07": ["geboren werden"],
    "2025-02-15": ["shutdown"]
}

# Funktion zum Anzeigen von Terminen
def show_appointments(year, month, day):
    date_str = f"{year}-{month:02}-{day:02}"
    if date_str in appointments:
        print(f"Termine für {date_str}:")
        for appointment in appointments[date_str]:
            print(f"- {appointment}")
    else:
        print(f"Keine Termine für {date_str}.")



