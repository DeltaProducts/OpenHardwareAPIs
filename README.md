## OpenHardwareAPIs
OpenHardwareAPIs - A set of Python APIs to control bare-metal switches fan,led,power,temperature sensors e.t.c.

## Synopsis
These APIs are written in python implemented by using ctypes to interface with C Language APIs provided by ONLP libraries.

## Code Example
#!/usr/bin/python
import libonlp
num_fans = libonlp.get_number_of_fans()
while(num_fans > 0):
  libonlp.set_fan_rpm(num_fans, 10000)
  num_fans = num_fans - 1
  
In the above example the libonlp is the python library which internally defines the functions get_numer_fans and set_fan_rpm. As can be seen in the function calls the set_fan_rpm function will set all the fans rpm in the switch to 10000.

## Motivation
The motivation for this is to give developer a way to interface with different components of the switch's hardware features.

## API Reference
The following are the list of APIs that will be provided by this python library.
# System information
get_system_info()
       --Returns the system information which can be accessed using sysinfo.getproductname(), sysinfo.getsoftwaversion e.t.c
       
# Thermal Sensors information.
num_of_therm_sensors = get_num_of_therm_sensors()
       --Returns number of sensors that are available in the system. The ids start from 1 to num_of_therm_sensors.
thermal = get_thermal_info(id)
       --Returns the thermal sensor object. The object has the following details which can be accessed by their corresponding get_xyz functions.
       thermal @ <id> = {
             Description: Thermal Sensor 2- close to sfp+ phy
             Status: 0x00000001 [ PRESENT ]
             Caps:   0x0000000f [ GET_TEMPERATURE,GET_WARNING_THRESHOLD,GET_ERROR_THRE
      SHOLD,GET_SHUTDOWN_THRESHOLD ]
             Temperature: 28875
             thresholds = {
                 Warning: 45000
                 Error: 55000
                 Shutdown: 60000
             }
         }
         
# System LEDs information.       
num_of_leds = get_num_of_sys_leds()
       --Returns number of leds that are available in the system. The ids start from 1 to num_of_leds.  
led = get_led_info(id)
       --Returns the led object. The object has the following details which can be accessed by their corresponding get_xyz functions.
       led @ <id> = {
         Description: sys
         Status: 0x00000005 [ PRESENT,ON ]
         Caps:   0x0003c000 [ YELLOW,YELLOW_BLINKING,GREEN,GREEN_BLINKING ]
         Mode: GREEN
         Char:
       }

set_led_state(id, state)
       --Sets the led state to either on or off based on the state passed.
set_led_mode(id, mode)
       --Sets the led mode.
set_led_char(id, char)
       --Sets the led character.
       
# Fan information.
num_of_fans = get_num_of_fans()
      --Returns number of fans that are available in the system. The ids start from 1 to num_of_fans.
fan  = get_fan_info(id)
      --Returns the led object. The object has the following details which can be accessed by their corresponding get_xyz functions.           fan @ <id> = {
       Description: Chassis Fan 3
       Status: 0x00000005 [ PRESENT,B2F ]
       Caps:   0x0000003c [ SET_RPM,SET_PERCENTAGE,GET_RPM,GET_PERCENTAGE ]
       RPM:    8057
       Per:    42
       Model:  ONLP_FAN_MODE_NORMAL
       SN:     NULL
      }
set_fan_rpm(id)
     --Sets the fan's speed in rpm.
set_fan_percentage(id)
     --Sets the fan's speed as a percentage.     
set_fan_mode(id)
     --Sets the fan's speed by mode.
set_fan_direction(id)
     --Sets the fan's direction.     
     
# SFP information.
Work In Progress.

# PSU information.
Work In Progress.


## Tests
Describe and show how to run the tests with code examples.

## License
A short snippet describing the license (MIT, Apache, etc.)
