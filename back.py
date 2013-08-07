#!/usr/bin/python2

# This is a personal script, quite unfinished to help me secure my computer
# state and personal files by way of automated/scripted backup solutions
# personalised to my [or your] system to allow for easy customisation of the
# output from the backup program itself [currently rdiff-backup].

# GPLv3, read LICENSE in ./

import sys
import subprocess

def conf(pac):   #create config file for the shell scripts
  conff = open('./conf.dat', 'w')
  conff.write('#!/usr/bin/bash\n\n')
  conff.write(pac+'\n\n')
  conff.write('if [ ! -d "$DIR" ]; then\n')
  conff.write('mkdir $DIR\nfi')
  conff.close()

def pacman():    #pacman stuff
  subprocess.call('./pacbac.sh')
  print 'Exported list of packages for pacman.'

def rdiff():     #rdiff-backup stuff
  subprocess.call('./rdbac.sh')
  print 'Rdiff-backup has performed its thing.'

def printhelp()
  print 'Not implemented yet.'
  exit
  
def main():      #main program
  if len(sys.argv) > 1:
    ne = 1
    if 'h' in sys.argv[1]:
      printhelp()
    elif not 'd' in arg and not 'f' in arg and not 'p' in arg:
      print 'Unknown option(s):' + sys.argv[1]
      printhelp()

  path = 'DIR=/home/d/.backup/'
  if ne and 'd' in sys.argv[1]:
    path = 'DIR='+raw_input('DIR=')

  conf(path)

  if ne:
    if 'p' in sys.argv[1]:
      pacman()
    if 'p' in sys.argv[1]:
      rdiff()

if __name__ == '__main__': # boilerplate run if called as program
  main()

