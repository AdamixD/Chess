import time

def get_now():
    sec = time.time()
    gmtime = time.gmtime(sec)
    return f"{gmtime.tm_hour:02}-{gmtime.tm_min:02}-{gmtime.tm_sec:02} {gmtime.tm_mday:02}.{gmtime.tm_mon:02}.{gmtime.tm_year}"
