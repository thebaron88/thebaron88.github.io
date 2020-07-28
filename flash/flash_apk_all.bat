@ECHO OFF
PATH=%PATH%;"%~dp0\platform-tools"

echo Flashing Chrome
call flash_apk_chrome.bat
echo Flashing Kiosk
call flash_apk_kiosk.
echo Flashing Sensor
call flash_apk_sensor.bat
echo Flashing ZXing
call flash_apk_zxing.bat