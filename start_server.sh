#!/bin/bash
docker build -t emotional_analysis_app .
docker run --name emotional_analysis_container -p 56563:56563 -v "$(pwd)":/app -d emotional_analysis_app
