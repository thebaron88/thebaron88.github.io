@ECHO OFF
PATH=%PATH%;"%~dp0\platform-tools"

adb install -t kiosk.apk
adb shell dpm set-device-owner "com.baron.kiosk/.MyDeviceAdminReceiver"