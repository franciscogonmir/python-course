import time


def calculate_go_home():
    hour_now = int(time.strftime("%H"))
    limit_hour = 19
    if hour_now > limit_hour:
        print("Is hour of go home")
    else:
        difference = limit_hour - hour_now
        print("{} hours left to go home".format(difference))


calculate_go_home()
