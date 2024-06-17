import subprocess
import os

def take_screenshot():
    try:
        path = 'screenshot.png'
        subprocess.run(['grim', path])
        print(f"Screenshot saved at {os.path.abspath(path)}")
    except Exception as e:
        print(f"An error occurred: {e}")

take_screenshot()
