@echo off
if "%~1"=="" (
  echo Usage: %0 text
  exit /b 1
)
set "text=%~1"
http POST http://127.0.0.1:56563/analyze_emotion text="%text%"
