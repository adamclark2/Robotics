#pragma once
#include <termios.h>
#include <unistd.h>
#include <stdlib.h>

/*
    Setup the terminal to receive constant input

    The distructor will revert the terminal to previous settings
*/
class ConstantInputTerminal {
    public:
        ConstantInputTerminal(){
            this->termios_orig = (struct termios*) malloc(sizeof(termios));

            struct termios termios_new;

            tcgetattr(STDOUT_FILENO, termios_orig);
            tcgetattr(STDOUT_FILENO, &termios_new);

            // https://linux.die.net/man/3/tcsetattr
            // Ctrl+F for the term 'Raw mode'
            termios_new.c_iflag &= ~(IGNBRK | BRKINT | PARMRK | ISTRIP| INLCR | IGNCR | ICRNL | IXON);
            termios_new.c_oflag &= ~OPOST;
            termios_new.c_lflag &= ~(ECHO | ECHONL | ICANON | ISIG | IEXTEN);
            tcsetattr(STDOUT_FILENO, TCSANOW, &termios_new);
        }

        ~ConstantInputTerminal(){
            tcsetattr(STDOUT_FILENO, TCSANOW, termios_orig);
            free((void*) termios_orig);
        }

    private:
        struct termios *termios_orig;
};