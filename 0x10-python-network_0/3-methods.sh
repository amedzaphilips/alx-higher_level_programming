#!/bin/bash
#prits allHTTP  methods a server allows
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
