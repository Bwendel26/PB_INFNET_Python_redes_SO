import psutil


def info_battery():
    battery = psutil.sensors_battery()
    return battery.percent

print(info_battery())