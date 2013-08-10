#!/usr/bin/bash

export DISPLAY=:0

COUNTER=0
while [  $COUNTER -lt 5 ]; do
  wmiir create /rbar/note &
  echo $1 | wmiir write /rbar/note
  sleep 1
  wmiir remove /rbar/note
  sleep 1
  let COUNTER=COUNTER+1 
done
