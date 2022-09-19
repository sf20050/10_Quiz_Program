import time


def countdown(time_min):
    while time_min:
        mint, sec = divmod(time_min, 60)
        time_format = '{:02d}:{:02d}'.format(mint, sec)
        print(time_format, end='\r')
        time.sleep(1)
        time_min -= 1

    print("stop")


countdown(10)
