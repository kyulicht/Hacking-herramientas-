import os
import subprocess

# Prompt the user to enter the IP address of the Android device
ADB_DEVICE_IP = input("Enter the IP address of the Android device: ")

# Connect to the device and take a screenshot
subprocess.call(f'adb -s {ADB_DEVICE_IP} shell screencap -p', shell=True)

# Save the screenshot to your computer
screenshot_name = "screenshot.png"
subprocess.call(f'adb -s {ADB_DEVICE_IP} pull /sdcard/{screenshot_name} ./{screenshot_name}', shell=True)

# Disconnect from the device
subprocess.call(f'adb -s {ADB_DEVICE_IP} kill-server', shell=True)

# Print success message
print(f"Screenshot saved as '{screenshot_name}'")