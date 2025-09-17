import psutil
import subprocess
import time

def notify(title, message):
    subprocess.run(["notify-send", title, message, "-u", "critical"])

while True:
    battery = psutil.sensors_battery()
    percent = battery.percent
    charging = battery.power_plugged

    if charging and percent >= 80:
        notify("Battery Full...80% Battery Charged ⚠️", "Please Unplug Adapter From Laptop.")

    time.sleep(120)