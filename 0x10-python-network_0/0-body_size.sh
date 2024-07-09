#!/bin/bash
# Sends and request and outputs count

curl -s "$1" | wc -c
