#!/usr/bin/python2

# Code by Damian A. Wloch, github.com/dami0, sracz0@gmail.com

# This is a personal script, quite unfinished to help me secure my computer
# state and personal files by way of automated/scripted backup solutions
# personalised to my [or your] system to allow for easy customisation of the
# output from the backup program itself [currently rdiff-backup].

# GPLv3, read LICENSE in ./

import sys
import subprocess
import re

def pacman(drt): #pacman script with directory passed from main
  subprocess.call(['./scripts/pacbac.sh', drt])
  print 'Exported list of packages for pacman.'

def rdiff(drt):  #rdiff-backup script with directory passed from main
  subprocess.call(['./scripts/rdbac.sh', drt])
  print 'Rdiff-backup has performed its thing.'

def printhelp(): #display help text and exit afterwards
  helpme = open('./help.me', 'rU')
  sys.stdout.write(helpme.read())
  helpme.close()
  exit()

def main():      #main program
  ne = 0 #assign sys.argv flag
  if len(sys.argv) > 1: #part of code responsible for help and unknowns
    ne = 1 #sys.argv flag on
    if re.findall('[^-dfphn]', sys.argv[1]): #code for unknowns, if ANY unknown
      print 'Unknown option(s): ' + str(match) + '\n' 
      printhelp() #display correct options as well
    if 'h' in sys.argv[1]: printhelp() #help option check

  path = '/home/d/.backup/' #standard dir, can be modified by user
  if ne and 'd' in sys.argv[1]:
    path = raw_input('DIR=') #user input for non-standard dir

  if ne and 'p' in sys.argv[1]: #running appropriate stuff at appropriate times
    pacman(path)
  if ne and 'f' in sys.argv[1]:
    rdiff(path)

  if ne: dty = 'Backonator has run with ' + sys.argv[1] + ' flags.' #wmii pager
  else: dty = 'Backonator has reconfigured.'                        #code
  subprocess.call(['./scripts/msg.sh', dty + '::3'])

if __name__ == '__main__': # boilerplate run if called as program
  main()

