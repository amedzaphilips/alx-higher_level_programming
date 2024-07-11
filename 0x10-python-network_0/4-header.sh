#!/bin/bash
#sends a GET request and displays body
curl -s "$1" | grep "X-School-User-Id"
