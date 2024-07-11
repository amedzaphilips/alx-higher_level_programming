#!/bin/bash
#prits allHTTP  methods a server allows
curl -sI "$1" | grep "Date" | cut -d " " -f2-
