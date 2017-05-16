## OpenHardwareAPIs
OpenHardwareAPIs - A set of Python APIs to control bare-metal switches fan,led,power,temperature sensors e.t.c.

## Synopsis
These APIs are written in python implemented by using ctypes to interface with C Language APIs provided by ONLP libraries.

## Code Example  

```
import libonlp
num_fans = libonlp.get_number_of_fans()
while(num_fans > 0):
  libonlp.set_fan_rpm(num_fans, 10000)
  num_fans = num_fans - 1
```  
In the above code example the libonlp is the python library which internally defines the functions get_number_fans and set_fan_rpm. As can be seen in the code, the set_fan_rpm function will set all the fans rpm in the switch to 10000.

## Motivation
The motivation for this is to give developer a way to control different features of the switch's hardware components.  


## API Reference
The following are the list of APIs that will be provided by this python library.

### System information
sys_info = get_system_info()  


       --Returns the system information.The returned object has the following details which can be accessed by their corresponding sys_info.get_xyz() function call.
       
       
       ```  
       System Information: = {
           Product Name: AG7648
           Serial Number: A766F0DL164S00031
           MAC: 00:18:23:30:d7:fa
           MAC Range: 256
           Manufacturer: DNI
           Manufacture Date: 04/30/2016 22:17:18
           Platform Name: x86_64-delta_ag7648-r0
           Country Code: CN
           Diag Version: 0.1
           ONIE Version: 2015.05-dirty
       }
       ```
   
### Thermal Sensors information.
num_of_therm_sensors = get_num_of_therm_sensors()


       --Returns number of sensors that are available in the system. The ids start from 1 to num_of_therm_sensors.
thermal = get_thermal_info(id)


       --Returns the thermal sensor object. The object has the following details which can be accessed by their corresponding thermal.get_xyz functions.
       
       
       ```
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
         ```
### System LEDs information.       
num_of_leds = get_num_of_sys_leds()


       --Returns number of leds that are available in the system. The ids start from 1 to num_of_leds.  
led = get_led_info(id)


        --Returns the led object. The object has the following details which can be accessed by their corresponding led.get_xyz functions.
        
        
      ```        
       led @ <id> = {
         Description: sys
         Status: 0x00000005 [ PRESENT,ON ]
         Caps:   0x0003c000 [ YELLOW,YELLOW_BLINKING,GREEN,GREEN_BLINKING ]
         Mode: GREEN
         Char:
       }
      ``` 
led.set_led(state)


       --Sets the led state to either on or off.  
       
led.set_led_color(color)


       --Sets the led color.
              
led.set_led_char(char)


       --Sets the led character.
       
### Fan information.
num_of_fans = get_num_of_fans()  


      --Returns number of fans that are available in the system. The ids start from 1 to num_of_fans.       
fan  = get_fan_info(id)  


      --Returns the fan object. The object has the following details which can be accessed by their corresponding fan.get_xyz functions.  
      
      
      ```
      fan @ <id> = {
       Description: Chassis Fan 3
       Status: 0x00000005 [ PRESENT,B2F ]
       Caps:   0x0000003c [ SET_RPM,SET_PERCENTAGE,GET_RPM,GET_PERCENTAGE ]
       RPM:    8057
       Per:    42
       Model:  ONLP_FAN_MODE_NORMAL
       SN:     NULL
      }
      ```
fan.set_fan_rpm(rpm)  


     --Sets the fan's speed in RPMs.       
     
     
fan.set_fan_percentage(percent)  

    --Sets the fan's speed as a percentage.  
    
fan.set_fan_mode(mode)  


    --Sets the fan's speed by mode.  
    
    
fan.set_fan_direction(dir)


     --Sets the fan's direction.  
 
     
###  SFP information.



### PSU information.


## Tests
Describe and show how to run the tests with code examples.

## License
A short snippet describing the license (MIT, Apache, etc.)
