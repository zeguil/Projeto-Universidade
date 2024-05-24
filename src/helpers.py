from datetime import datetime

def format_date(date: str) -> datetime.date:
    date_splitted = date.split("-")
    return datetime(int(date_splitted[0]), int(date_splitted[1]), int(date_splitted[2])).date()    