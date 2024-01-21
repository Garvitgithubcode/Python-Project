# Drink water remainder 
# For all type of operating system Ex:- Windows, MacOS, Linux 
import time
import platform
from plyer import notification 

def remind_to_drink_water():
    while True:
        # Adjust the interval based on your preference (in seconds)
        time.sleep(60 * 60)  # Remind every 1 hour

        # Check the operating system and trigger the reminder
        if platform.system() == "Windows":
            import winsound
            winsound.MessageBeep()  # Beep sound on Windows
            notification.notify(
                title="Drink Water",
                message="Remember to drink water!",
                timeout=1
            )
        elif platform.system() == "Darwin":  # macOS
            notification.notify(
                title="Drink Water",
                message="Remember to drink water!",
                timeout=10
            )
        elif platform.system() == "Linux":
            notification.notify(
                title="Drink Water",
                message="Remember to drink water!",
                app_icon=None,  # Path
                timeout=10
            )

if __name__ == "__main__":
    remind_to_drink_water()
