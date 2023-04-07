@echo off
docker build -t emotional_analysis_app .
docker run --name emotional_analysis_container -p 56563:56563 -v %cd%:/app -d emotional_analysis_app
