#!/usr/bin/python2

# This is a personal script, quite unfinished to help me secure my computer
# state and personal files by way of automated/scripted backup solutions
# personalised to my [or your] system to allow for easy customisation of the
# output from the backup program itself [currently rdiff-backup].

# GPLv3, read LICENSE in ./

import sys
import subprocess
import re

def conf(pac):   #create config file for the shell scripts
  conff = open('./conf.dat', 'w')
  conff.write('#!/usr/bin/bash\n\n')
  conff.write(pac+'\n\n')
  conff.write('if [ ! -d "$DIR" ]; then\n')
  conff.write('mkdir $DIR\nfi')
  conff.close()

def pacman():    #pacman stuff
  subprocess.call('./scripts/pacbac.sh')
  print 'Exported list of packages for pacman.'

def rdiff():     #rdiff-backup stuff
  subprocess.call('./scripts/rdbac.sh')
  print 'Rdiff-backup has performed its thing.'

def printhelp():
  helpme = open('./help.me', 'r')
  for line in helpme.readlines():
    print line.rstrip('\n')
#  sys.stdout.write(helpme.read())
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

  path = 'DIR=/home/d/.backup/'
  if ne and 'd' in sys.argv[1]:
    path = 'DIR='+raw_input('DIR=')

  conf(path)

  if ne:
    if 'p' in sys.argv[1]:
      pacman()
    if 'f' in sys.argv[1]:
      rdiff()

if __name__ == '__main__': # boilerplate run if called as program
  main()

