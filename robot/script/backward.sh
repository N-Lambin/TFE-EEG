#!/bin/sh

export MC1=/sys/class/tacho-motor/motor1
echo reset > $MC1/command
echo -1000 > $MC1/speed_sp
echo 1000 > $MC1/time_sp
echo run-timed > $MC1/command

export MC2=/sys/class/tacho-motor/motor2
echo reset > $MC2/command
echo -1000 > $MC2/speed_sp
echo 1000 > $MC2/time_sp
echo run-timed > $MC2/command