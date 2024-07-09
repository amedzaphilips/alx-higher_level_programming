#!/usr/bin/bash

response_body=$(curl -s "$1")
length=${#response_body}
echo "$length"
