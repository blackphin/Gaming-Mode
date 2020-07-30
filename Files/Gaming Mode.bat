@echo off
tasklist /FI "IMAGENAME eq steam.exe" 2>NUL | find /I /N "steam.exe">NUL
if "%ERRORLEVEL%"=="0" goto Process_Found
tasklist /FI "IMAGENAME eq EpicGamesLauncher.exe" 2>NUL | find /I /N "EpicGamesLauncher.exe">NUL
if "%ERRORLEVEL%"=="0" goto Process_Found
:Process_NotFound
taskkill /IM googledrivesync.exe /T /F
taskkill /IM OneDrive.exe /T /F
taskkill /IM Chrome.exe /T /F
taskkill /IM WhatsApp.exe /T /F
taskkill /IM AnyDesk.exe /T /F
start "" "C:\Users\shiva\AppData\Local\Discord\Update.exe"
start "" "C:\Users\shiva\AppData\Local\Discord\app-0.0.306\Discord.exe"
goto END
:Process_Found
taskkill /IM steam.exe /T /F
taskkill /IM EpicGamesLauncher.exe /T /F
start "" "C:\Program Files\Google\Drive\googledrivesync.exe"
start "" "C:\Users\shiva\AppData\Local\Microsoft\OneDrive\OneDrive.exe"
timeout 2
wscript "D:\Program Files (x86)\Gaming-Mode\Files\autokey.vbs"
:END
Exit