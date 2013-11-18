/*
 * ===== SOURCE FILE ==========================================
 *
 *          Filename:  ptii.c
 *            Author:  Willy Goiffon
 *
 *     Creation Date:  04-05-2013 14:39:19
 *     Last Modified:  mar. 07 mai 2013 15:01:27 CEST
 *          Compiler:  tcc
 *
 *       Description:  write dynamically into a pipe 'ii'
 *                     located in the current directory.
 *                     End ptii by typing /q or /x.
 *                     Clear the screen with /c.
 *
 *                     Light but/yet powerful, meant to play 
 *                     with ii nicely !
 *
 * ============================================================
 */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/fcntl.h>

int
operations(int file_desc) {

    char buf[256];

    while (!feof(stdin) ) {
        /* Command prompt */
        printf("] ");
        fgets(buf, 255, stdin);

        if (buf[0] == '/') {
            switch(buf[1]) {
                case 'x': /* so you can end ptii without closing irc */
                    return 0;
                case 'c': /* here you do that thing where you switch channel */
                    // maybe have a channel selector here somehow
                    return 1;
                case 's': /* here we switch server */
                    // switch server variable?
                    return 2;
                default: break;
            }
        }

        if (write(file_desc, buf, strlen(buf)) < 0 ) {
            perror("write");
            exit(1);
        }

    }
}

int
main(int argc, const char **argv) {

    int fd = 1, act;

    fd = open("in", O_WRONLY); /* pipe opened for reading */
    if (fd > 0) { 
        act = operations(fd);
        printf("The magic number is: %d\n", act);  
    } else if(fd < 0){ 
        fputs("cannot open pipe\n", stderr);
    }
    return 0;
}
