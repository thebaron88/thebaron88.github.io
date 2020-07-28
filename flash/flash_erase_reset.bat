@ECHO OFF
PATH=%PATH%;"%~dp0\platform-tools"
rem 7z x platform-tools_r26.0.2-windows.zip

adb reboot bootloader
fastboot boot twrp-3.4.0-0-mako.img

echo Press any key when recovery has booted
pause >nul

adb shell twrp wipe cache
adb shell twrp wipe dalvik
adb shell twrp wipe data

adb reboot system

echo Press any key when adb is enabled on the device
pause >nul

adb install sensors.apk

echo Press any key to exit...
pause >nul
exit