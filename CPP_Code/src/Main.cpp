#include <stdio.h>

#include "ConstantInputTerminal.cpp"
// #include "RobotControl.cpp"
#include "RobotControlEv3.cpp"

#define CTRL_C 3

ConstantInputTerminal* cit;

/* Cleanup malloc'd globals */
void cleanupAndQuit(){
    delete cit;
    exit(0);
}

int main(int argc,char** argv){
    cit = new ConstantInputTerminal();
    RobotControlEv3* remote = new RobotControlEv3();

    printf("Use WASD to control the robot. Press ctrl+c to quit or the letter 'Q' \r\n"
           "---------------------------------------------------------------------\r\n");

    bool quit = false;
    int i = 0;
    while(!quit){
        char c;
        if(i > 5){ // Replace this with delta time if need be
            remote->stop();
            i = 0;
        }
        read(STDIN_FILENO, &c, 1);

        /*
            I think this is good.
            If we need a ton of inputs then we can
            write a lookup table.

            ...
            This is for testing
        */
        if(c == 'q' || c == 'Q'){
            quit = true;
        } else if(c == 'w' || c == 'W'){
            remote->up();
            i--;
        } else if(c == 'a' || c == 'A'){
            remote->left();
            i--;
        } else if(c == 'd' || c == 'D'){
            remote->right();
            i--;
        } else if(c == 's' || c == 'S'){
            remote->down();
            i--;
        } else if(c == CTRL_C) {
            quit=true;
        }else{
            printf("char [%c] has char code [%d]\r\n", c, (int) c);
        }
        i++;
    }

    delete remote;
    cleanupAndQuit();
}