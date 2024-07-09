#!/bin/bash
# Sends and request and outputs count

curl -s -o /dev/null -w '%{size_download}\n' "$1"
