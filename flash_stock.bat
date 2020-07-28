@ECHO OFF
PATH=%PATH%;"%~dp0\platform-tools"
rem 7z x platform-tools_r26.0.2-windows.zip
rem 7z x occam-lmy48t-factory-c43c7cfd.zip

adb reboot bootloader
cd occam-lmy48t
call flash-all.bat
cd ..