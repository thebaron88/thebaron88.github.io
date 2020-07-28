@ECHO OFF
PATH=%PATH%;"D:\platform-tools_r30.0.3-windows\platform-tools_r26.0.2-windows\platform-tools"

adb reboot bootloader
rem fastboot flash recovery twrp-3.4.0-0-mako.img
fastboot boot twrp-3.4.0-0-mako.img
adb shell twrp wipe cache
adb shell twrp wipe dalvik
adb shell twrp wipe data
adb shell mkdir /cache/recovery
adb push lineage-16.0-20200713-UNOFFICIAL-mako.zip /sdcard/
adb shell twrp install /sdcard/lineage-16.0-20200713-UNOFFICIAL-mako.zip
adb reboot system
rem adb sideload lineage-16.0-20200713-UNOFFICIAL-mako.zip

!!! Turn on ADB
adb install sensors.apk

echo Press any key to exit...
pause >nul
exit




fastboot boot twrp-3.4.0-0-mako.img
adb shell twrp wipe cache
adb shell twrp wipe dalvik
adb shell twrp wipe data
adb shell mkdir /cache/recovery
adb shell twrp sideload
adb sideload lineage-17.1-20200713-UNOFFICIAL-mako.zip
adb reboot system
rem adb sideload lineage-16.0-20200713-UNOFFICIAL-mako.zip

!! Turn on ADB
adb install sensors.apk

!! Test sensors
adb install barcode.apk
adb install kiosk.apk




7z x occam-lmy48t-factory-c43c7cfd.zip
call occam-lmy48t\flash-all.bat.bat