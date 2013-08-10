#!/usr/bin/python2

# This is a personal script, quite unfinished to help me secure my computer
# state and personal files by way of automated/scripted backup solutions
# personalised to my [or your] system to allow for easy customisation of the
# output from the backup program itself [currently rdiff-backup].

# GPLv3, read LICENSE in ./

import sys
import subprocess
import re

def pacman(drt): #pacman stuff
  subprocess.call(['./scripts/pacbac.sh', drt])
  print 'Exported list of packages for pacman.'

def rdiff(drt):  #rdiff-backup stuff
  subprocess.call(['./scripts/rdbac.sh', drt])
  print 'Rdiff-backup has performed its thing.'

def printhelp():
  helpme = open('./help.me', 'rU')
  sys.stdout.write(helpme.read())
  helpme.close()
  exit()

def main():      #main program
  ne = 0
  if len(sys.argv) > 1:
    ne = 1
    match = re.findall('[^-dfphn]', sys.argv[1])
    if match:
      print 'Unknown option(s): ' + str(match) + '\n'
      printhelp()
    if 'h' in sys.argv[1]: printhelp()

  path = '/home/d/.backup/'
  if ne and 'd' in sys.argv[1]:
    path = raw_input('DIR=')

  if ne and 'p' in sys.argv[1]:
    pacman(path)
  if ne and 'f' in sys.argv[1]:
    rdiff(path)

  if ne: dty = 'Backonator has run with ' + sys.argv[1] + ' flags.'
  else: dty = 'Backonator has reconfigured'
  subprocess.call(['./scripts/msg.sh', dty + '::3'])

if __name__ == '__main__': # boilerplate run if called as program
  main()

