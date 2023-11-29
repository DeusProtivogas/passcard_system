import datetime


def is_visit_long(duration, suspicious_time=None):
    if not suspicious_time:
        suspicious_time = datetime.timedelta(minutes=60)
    return duration >= suspicious_time


def format_duration(duration):
    seconds = duration.total_seconds()
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    return f"{hours}ч:{minutes}м"
