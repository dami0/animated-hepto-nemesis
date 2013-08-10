#!/usr/bin/sh

MSG=TEST

wmiir create /rbar/note &

echo $MSG | wmiir write /rbar/note
