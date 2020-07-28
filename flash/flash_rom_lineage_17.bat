@ECHO OFF
PATH=%PATH%;"%~dp0\platform-tools"
rem 7z x platform-tools_r26.0.2-windows.zip

echo Rebooting to bootloader
adb reboot bootloader
echo Booting to recovery
fastboot boot twrp-3.4.0-0-mako.img

echo Press any key when recovery has booted
pause >nul

echo Wiping Things
adb shell twrp wipe cache
adb shell twrp wipe dalvik
adb shell twrp wipe data
adb shell mkdir /cache/recovery
echo Starting Sideload Service
adb shell twrp sideload

echo Press any key when sideload is ready
pause >nul

echo Doing Sideload
adb sideload lineage-17.1-20200713-UNOFFICIAL-mako.zip
echo Rebooting into ROM
adb reboot system

echo Press any key when adb is enabled on the device
pause >nul

echo Flashing all applications
call flash_apk_all.bat

echo Press any key to exit...
pause >nul
exit