import Timetable

def print_buses():
    next_buses = Timeline.get_buses
    for ride in next_buses:
        print("{line}: {time}Min, ".format(line = ride[0], time = ride[2]), \
            end = "")
