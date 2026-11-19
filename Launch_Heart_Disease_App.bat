@echo off
title CARDIOPULSE AI - Heart Disease Diagnostic Launcher
color 0C
echo ========================================================
echo   CARDIOPULSE AI - HEART DISEASE DIAGNOSTIC LAUNCHER
echo   Author: Philip Antwi - Pentecost University
echo ========================================================
echo.
echo Choose how you want to run the Heart Disease Diagnostic App:
echo.
echo   [1] Open Live Cloud App in Browser (GitHub Pages)
echo   [2] Launch Local Interactive Web App (http://localhost:8080)
echo   [3] Open Vercel Project Console
echo   [4] Open Online VS Code Web Editor (github.dev)
echo   [5] Exit
echo.
set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" (
    echo Opening live cloud app...
    start https://philipntwi-bot.github.io/Heart_Disease_Classification_Project/
    goto end
)
if "%choice%"=="2" (
    echo Starting local web server on port 8080...
    start http://localhost:8080/index.html
    py -3 -m http.server 8080
    goto end
)
if "%choice%"=="3" (
    echo Opening Vercel Project Console...
    start https://vercel.com/philipntwi-bot/heart-disease-classification-project
    goto end
)
if "%choice%"=="4" (
    echo Opening GitHub.dev online web editor...
    start https://github.dev/Philipntwi-bot/Heart_Disease_Classification_Project
    goto end
)

:end
