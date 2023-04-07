#!/bin/bash
if [ $# -eq 0 ]; then
  echo "Usage: $0 text"
  exit 1
fi
text="$1"
curl --header "Content-Type: application/json" --request POST --data "{\"text\":\"$text\"}" http://127.0.0.1:56563/analyze_emotion
