#!/usr/bin/python2

import subprocess

def main():
  newlist = [] #list for rewriting the file
  msg_list = open('/home/d/.msg/notelist', 'rU') #open list of stuff to display
  for line in msg_list.readlines():
    curr = line.split('::') #seperate message from number of time to display
    if len(curr) > 1: #check to make sure message is formatted properly
      if '::k' not in line: curr[1] = int(curr[1].strip('\n')) #extract the
      if '::k' not in line: curr[1] -= 1                       #display time
      subprocess.call(['/home/d/python/ahn/pager/wmiir.sh', curr[0]]) #script
      newlist.append(curr[0] + '::' + str(curr[1]) + '\n') #Generate message -1
  msg_list.close()

  msg_list = open('/home/d/.msg/notelist', 'w') #regenerate the notelist
  for line in newlist:
    if '::0' not in line: #drop after run through x times
      msg_list.write(line)
  msg_list.close()

if __name__ == '__main__': # boilerplate run if called as program
  main()
