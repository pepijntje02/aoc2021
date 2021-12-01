:: do not show commands when the batch file runs
@echo off 
echo "Download AoC2020 puzzle"

set /p id="Which day is it: "
set URL="https://adventofcode.com/2021/day/%id%/input"
set dirName=%~dp0day%id%\

if not exist %dirName% mkdir %dirName%

echo %~dp0boilerplate.py
echo %dirName%day%id%.py

echo F | xcopy %~dp0boilerplate.py %dirName%day%id%.py

curl %URL% --output %dirName%input.txt --cookie %~dp0settings\cookies.txt 
echo "Bye!"