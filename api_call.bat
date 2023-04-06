@echo off
set /p text=Enter text: 
http POST http://127.0.0.1:56563/analyze_emotion text="%text%"
