#pragma once
#include <stdio.h>
#include <stdint.h>

// #include "RobotControl.cpp"

#include "ev3.h"
#include "ev3_port.h"
#include "ev3_tacho.h"

#define RIGHT OUTPUT_C
#define LEFT OUTPUT_B

/*
    A simple class to control a robot. Think of this as a 
    remote with up,down,right,left
*/
class RobotControlEv3 {
    public:
        RobotControlEv3(){
            // init ev3 here?
            if ( ev3_init() == -1 ){
                printf("Init failed!\n");
            }
            while ( ev3_tacho_init() < 1 ) {
                // busy loop
            }

            ev3_search_tacho_plugged_in(LEFT, EXT_PORT__NONE_, &(this->leftSn), 0 );
            ev3_search_tacho_plugged_in(RIGHT,EXT_PORT__NONE_, &(this->rightSn), 0 );

            set_tacho_stop_action_inx( rightSn, TACHO_RESET );
            set_tacho_stop_action_inx( leftSn,  TACHO_RESET );
            set_tacho_stop_action_inx( rightSn, TACHO_RUN_FOREVER );
            set_tacho_stop_action_inx( leftSn,  TACHO_RUN_FOREVER );

            get_tacho_max_speed( rightSn, &rightMaxSpeed );
            get_tacho_max_speed( leftSn, &rightMaxSpeed );
        }

        ~RobotControlEv3(){
            // de-init ev3 here?
            ev3_uninit();
        }

        void up(){
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
            set_tacho_speed_sp( rightSn, 0 );
            set_tacho_speed_sp( leftSn, 0  );
            set_tacho_stop_action_inx( leftSn, TACHO_RUN_FOREVER );
            set_tacho_stop_action_inx( rightSn, TACHO_RUN_FOREVER );
        }

    private:
        uint8_t rightSn;
        uint8_t leftSn;
        int rightMaxSpeed;
        int leftMaxSpeed;
        

        /* Set the speed of the right motor
        this should be +/- 255
        */
        void setRightMotor(int speed){
            speed = clamp(speed);
            //set_tacho_speed_sp( rightSn, (int) (rightMaxSpeed * (speed/255.0)) );
            set_tacho_speed_sp( rightSn, 1050 );
            set_tacho_stop_action_inx( rightSn, TACHO_RUN_FOREVER );
        }

        /* Set the speed of the left motor
        this should be +/- 255
        */
        void setLeftMotor(int speed){
            speed = clamp(speed);
            set_tacho_speed_sp( leftSn,  1050 );
            set_tacho_stop_action_inx( leftSn, TACHO_RUN_FOREVER );
        }

        /* Assert input values are correct */
        int clamp(int value){
            value = value > 255 ? 255 : value;
            value = value < -255 ? -255 : value;
            return value;
        }
};