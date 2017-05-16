## OpenHardwareAPIs
OpenHardwareAPIs - A set of Python APIs to control bare-metal switches fan,led,power,temperature sensors e.t.c.

## Synopsis
These APIs are written in python implemented by using ctypes to interface with C Language APIs provided by ONLP libraries.

## Code Example  


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
 
     
###  {Q}SFP information.
num_sfp_ports = get_number_of_sfp_ports()

      --Return number of ports that are {Q}SFP-capable.

sfp = get_sfp_info(port)

      --Returns the sfp object. The object has the following attributes which can be accessed by their corresponding sfp.get_xyz().
      ```
      Port 1: Present, Status = 0x00000014 [ RX_LOS,TX_DISABLE ]
      eeprom:
        0000: 0d 00 04 00 00 00 00 00 00 00 00 00 00 00 00 00
        0010: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        0020: 00 00 43 4d 50 51 41 41 50 43 41 41 33 37 2d 31
        0030: 33 32 32 2d 30 31 56 30 31 20 51 53 46 50 2d 48
        0040: 34 30 47 2d 43 55 31 4d 20 20 20 20 20 20 00 00
        0050: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        0060: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        0070: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        0080: 0d 00 23 08 00 00 00 00 00 00 00 05 67 00 00 00
        0090: 00 00 01 a0 4f 45 4d 20 20 20 20 20 20 20 20 20
        00a0: 20 20 20 20 00 a8 b0 ae 51 53 46 50 2d 48 34 30
        00b0: 47 2d 43 55 32 4d 20 20 30 32 03 04 00 00 46 59
        00c0: 00 00 00 00 48 4c 31 36 30 36 30 33 30 32 36 20
        00d0: 20 20 20 20 31 31 31 32 32 33 30 30 00 00 00 86
        00e0: 00 00 1c 37 90 79 36 75 6f 77 8f 57 77 b7 e1 8f
        00f0: fa 8f 14 00 00 00 00 00 00 00 00 00 1d 27 dd 33
     ```      

### PSU information.
num_of_psus = get_num_of_psus()


       --Returns number of PSUs that are available in the system. The ids start from 1 to num_of_psus.
psu = get_psu_info(id)


       --Returns the psu object. The object has the following details which can be accessed by their corresponding psu.get_xyz functions.
       
       
       ```
       psu @ 1 = {
           Description: PSU-1
           Model:  00007
           SN:     81 
           Status: 0x00000005 [ PRESENT,UNPLUGGED ]
           Caps:   0x00000000
           Vin:    116750
           Vout:   12023
           Iin:    761
           Iout:   6375
           Pin:    88500
           Pout:   76625
       }

         ```

## Tests

```
import libonlp
num_fans = libonlp.get_number_of_fans()
while(num_fans > 0):
  libonlp.set_fan_rpm(num_fans, 10000)
  num_fans = num_fans - 1
```

In the above code example the libonlp is the python library which internally defines the functions get_number_fans and set_fan_rpm. As can be seen in the code, the set_fan_rpm function will set all the fans rpm in the switch to 10000.

## License
Work In Progress..
