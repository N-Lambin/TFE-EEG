#!/bin/sh

export MC3=/sys/class/tacho-motor/motor3
echo reset > $MC3/command
echo -700 > $MC3/speed_sp
echo 500 > $MC3/time_sp
echo run-timed > $MC3/command