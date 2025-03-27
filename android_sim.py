import subprocess
import time
import os

# Adjust these paths
EMULATOR_PATH = r"C:\Users\Anjali\AppData\Local\Android\Sdk\emulator\emulator.exe"
AVD_NAME = "Pixel_5_API_30"
ADB_PATH = r"C:\Users\Anjali\AppData\Local\Android\Sdk\platform-tools\adb.exe"
APK_PATH = r"C:\Users\Anjali\Downloads\Calculator_8.6.1 (625857114)_APKPure.apk"

def start_emulator():
    print("🚀 Starting emulator...")
    subprocess.Popen([EMULATOR_PATH, "-avd", AVD_NAME])
    time.sleep(60)  # Give emulator time to boot up

def install_apk():
    print("📦 Installing APK...")
    subprocess.run([ADB_PATH, "install", APK_PATH])

def get_device_info():
    print("📋 Fetching device info...")
    subprocess.run([ADB_PATH, "shell", "getprop"])

if __name__ == "__main__":
    start_emulator()
    install_apk()
    get_device_info()
