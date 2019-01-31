# Robotics
Code related to `COS 389 Robotics`. Requires a `ev3 robot` and `ev3dev linux`
on said robot.

# Folders & What they do

|Folder     |What it does                                                            |
|-----------|------------------------------------------------------------------------|
|CPP_Cod e  |c++ code for the robot, currently doesn't work due to config            |
|Bash_Code  |Bash scripts to control the robot                                       |
|Python_Code|Code written in python                                                  |

# Remote control the bot

        Connect the robot via usb or blutooth
        ssh into the robot
        run the script ./Bash_code/RemoteControl.sh

# Useful Shell Code

        ssh robot@ev3dev.local
        scp -r ./* robot@ev3dev.local:Code

# Useful Links
https://www.ev3dev.org/docs/tutorials/tacho-motors/  
http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-jessie/motors.html#tacho-motor-subsystem  
http://in4lio.github.io/ev3dev-c/group__ev3__port.html  
  
https://www.ev3dev.org/docs/tutorials/  
  
https://www.ev3dev.org/docs/tutorials/connecting-to-ev3dev-with-ssh/  
https://www.ev3dev.org/docs/tutorials/connecting-to-the-internet-via-bluetooth/  
https://www.ev3dev.org/docs/tutorials/connecting-to-the-internet-via-usb/  
https://www.ev3dev.org/docs/tutorials/using-bluetooth-tethering/  

