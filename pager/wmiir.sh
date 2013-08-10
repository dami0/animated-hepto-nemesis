#!/usr/bin/sh

wmiir create /rbar/note &
echo $1 | wmiir write /rbar/note
sleep 1
wmiir remove /rbar/note
sleep 1
wmiir create /rbar/note &
echo $1 | wmiir write /rbar/note
sleep 1
wmiir remove /rbar/note
sleep 1  
wmiir create /rbar/note &
echo $1 | wmiir write /rbar/note
sleep 1
wmiir remove /rbar/note
