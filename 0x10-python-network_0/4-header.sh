#!/bin/bash
#sends a GET request and displays body
curl -sI "$1" | grep "X-School-User-Id"
