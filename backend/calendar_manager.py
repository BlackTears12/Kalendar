from gcsa.google_calendar import GoogleCalendar


class CalendarManager:
    def __init__(self,email_address: str):
        self.calendar = GoogleCalendar(email_address)
        for event in self.calendar:
            print(event)
