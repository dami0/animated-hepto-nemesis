#!/usr/bin/python2

# This is a personal script, quite unfinished to help me secure my computer
# state and personal files by way of automated/scripted backup solutions
# personalised to my [or your] system to allow for easy customisation of the
# output from the backup program itself [currently rdiff-backup].

import sys
import subprocess

def conf(pac): #create config file for the shell scripts
  conff = open('./conf.dat', 'w')
  conff.write('#!/usr/bin/bash\n\n')
  conff.write(pac+'\n')
  conff.close()

def pacman():
  subprocess.call('./pacbac.sh')
  print 'Exported list of packages for pacman.'

def rdiff():
  subprocess.call('./rdbac.sh')
  print 'Rdiff-backup has performed its thing.'

def main(): #probably want to put configuration and state in here
  path = 'DIR=/home/d/.backup/'
  if len(sys.argv) >= 2:
    if 'd' in sys.argv[1]:
      path = 'DIR='+raw_input('DIR=')

#  conf(path)

#  pacman()

  if len(sys.argv) >= 2:
    if 'f' in sys.argv[1]:
      rdiff()

if __name__ == '__main__': # boilerplate run if called as program
  main()
