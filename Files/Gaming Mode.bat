@echo off
taskkill /IM googledrivesync.exe /T /F
taskkill /IM OneDrive.exe /T /F
taskkill /IM Chrome.exe /T /F
taskkill /IM WhatsApp.exe /T /F
taskkill /IM AnyDesk.exe /T /F
taskkill /IM Zoom.exe /T /F
cd C:\Users\shiva\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\
start discord
Exit