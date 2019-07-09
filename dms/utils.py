from datetime import datetime, timedelta


def kst_now():
    return datetime.utcnow() + timedelta(hours=9)
