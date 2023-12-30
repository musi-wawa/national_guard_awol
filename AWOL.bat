@echo off
mode con: cols=80 lines=25

set "python_exe=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"

if not exist "%python_exe%" (
    echo Python executable not found. Please install Python or update the path in this script.
    pause
    exit /b 1
)

"%python_exe%" ng-awol.py

pause
