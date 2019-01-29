#pragma once
#include <stdio.h>
#include <stdint.h>

/*
    A simple class to control a robot. Think of this as a 
    remote with up,down,right,left
*/
class RobotControl {
    public:
        RobotControl(){
            // init ev3 here?
        }

        ~RobotControl(){
            // de-init ev3 here?
        }

        void up(){
            printf("UP!\r\n");
            setRightMotor(255);
            setLeftMotor(255);
        }

        void down(){
            setRightMotor(-255);
            setLeftMotor(-255);
        }

        void right(){
            setRightMotor(-255);
            setLeftMotor(255);
        }

        void left(){
            setRightMotor(255);
            setLeftMotor(-255);
        }

        void stop(){
            // todo
        }

    private:
        /* Set the speed of the right motor
        this should be +/- 255
        */
        void setRightMotor(int speed){
            speed = clamp(speed);
            // todo
        }

        /* Set the speed of the left motor
        this should be +/- 255
        */
        void setLeftMotor(int speed){
            speed = clamp(speed);
            // todo
        }

        /* Assert input values are correct */
        int clamp(int value){
            value = value > 255 ? 255 : value;
            value = value < -255 ? -255 : value;
            return value;
        }
};