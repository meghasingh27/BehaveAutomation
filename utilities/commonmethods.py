from datetime import datetime


def get_current_datetime():
    time_stamp = datetime.now().strftime("%m/%d/%Y_%H:%M:%S")
    return time_stamp