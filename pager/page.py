#!/usr/bin/python2

import subprocess

def main():
  newlist = []
  msg_list = open('/home/d/.msg/notelist', 'rU')
  for line in msg_list.readlines():
    print line
    curr = line.split('::')
    if len(curr) > 1:
      curr[1] = int(curr[1].strip('\n'))
      curr[1] -= 1
      subprocess.call(['./wmiir.sh', curr[0]])
      newlist.append(curr[0] + '::' + str(curr[1]) + '\n')
  msg_list.close()

  msg_list = open('/home/d/.msg/notelist', 'w')
  for line in newlist:
    if '::0' not in line:
      msg_list.write(line)
  msg_list.close()

if __name__ == '__main__': # boilerplate run if called as program
  main()
