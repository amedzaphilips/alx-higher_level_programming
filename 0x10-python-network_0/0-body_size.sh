#!/bin/bash
# Sends and request and outputs count

response_body=$(curl -s "$1")
length=${#response_body}
echo "$length"
