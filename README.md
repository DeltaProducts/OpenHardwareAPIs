## OpenHardwareAPIs
OpenHardwareAPIs - A set of Python APIs to control bare-metal switches fan,led,power,temperature sensors e.t.c.

## Synopsis
These APIs are written in python implemented by using ctypes to interface with C Language APIs provided by ONLP libraries.

## Tests
      
      The following test sample uses the APIs to access the fan properties and control the fan's rpm.
```
import libonlp
fans = libonlp.get_fans()
count = fans.len()
while(count > 0):
  fans[count].set_rpm(10000)
  print fans[count].description()
  count = count - 1
```

## Code Example 
Following code is to redefine the “C” structures, in ONLP library, to python
```
class libonlp:
    def __init__():
          libonlp = ctypes.CDLL('/lib/x86_64-linux-gnu/libonlp.so')
          libonlp.onlp_fan_info_get.argtypes = [ctypes.c_uint, ctypes.POINTER(onlp_fainfo_t)]
          libonlp.onlp_fan_info_get.restype = ctypes.c_int
          .....//leds/sfp/psus.. will also be initialized here.
          
class onlp_fan_info_t(ctypes.Structure): // Similar structures need to be defined for other onlp supported components.
   _fields_ = [("hdr", onlp_oid_hdr),
              ("status", ctypes.c_uint),
              ("caps", ctypes.c_uint),
              ("rpm", ctypes.c_int),
              ("percentage", ctypes.c_int),
              ("mode", ctypes.c_int),
              ("model", ctypes.c_char * 64),
              ("serial",ctypes.c_char * 64)]   
              
              
def get_fans():
    id = 1
    while(true):
      fan = fan(id)
      status = fan.status
      if(status):
         fanlist.append(fan)
      else:
         break
      id = id + 1
    return fanlist
    
class fan(object):
    fanoid = 0x3000000
    onlp_fan = onlp_fan_info_t()
    def __init__(self, fanid):
        self.fanoid = self.fanoid | fanid
        libonlp.onlp_fan_init()
        self.obj = libfan.onlp_fan_info_get(self.fanoid, ctypes.byref(self.onlp_fan))
    def set_rpm(self, rpm):
        libonlp.onlp_fan_init()
        libonlp.onlp_fan_rpm_set(self.fanoid, rpm)
        self.obj = libfan.onlp_fan_info_get(self.fanoid, ctypes.byref(self.onlp_fan))

```

## Motivation
Motivation for this library is to give developer a way to control and validate different features of the switch's hardware components.


## API Reference
Following are initial list of APIs that will be provided by this python library.  In the future these libraries may be expanded to other components.”

### System information
sys_info = get_system_info()  


       --Returns the system information object.The object has the following details which 
         can be accessed by their corresponding names.
       
       
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
therms = get_thermal_sensors()


       --Returns list of thermal sensor objects that are available in the system. The list can be accessed by therms[1].The object has the following details which can be accessed by their corresponding names.
       
       
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
leds = get_leds()


       --Returns list of led objects that are available in the system. The list can be accessed by therms[1].The object has the following details which can be accessed by their corresponding names.
        
        
      ```        
       led @ <id> = {
         Description: sys
         Status: 0x00000005 [ PRESENT,ON ]
         Caps:   0x0003c000 [ YELLOW,YELLOW_BLINKING,GREEN,GREEN_BLINKING ]
         Mode: GREEN
         Char:
       }
      ``` 
led.set_state(state)


       --Sets the led state to either on or off.  
       
led.set_color(color)


       --Sets the led color.
              
led.set_char(char)


       --Sets the led character.
       
### Fan information.
fans = get_fans()  


      --Returns the list of fan objects. The object has the following details which 
        can be accessed by their corresponding names.  
      
      
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
fan.set_rpm(rpm)  


     --Sets the fan's speed in RPMs.       
     
     
fan.set_percentage(percent)  

    --Sets the fan's speed as a percentage.  
    
fan.set_mode(mode)  


    --Sets the fan's speed by mode.  
    
    
fan.set_direction(dir)


     --Sets the fan's direction.  
 
     
###  {Q}SFP information.
sfps = get_sfp_ports()

      --Returns the list of sfp object. The object has the following attributes which 
        can be accessed by their corresponding names.
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
psus = get_psus()


      --Returns the list of psu object. The object has the following attributes which 
        can be accessed by their corresponding names.       
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



In the code example above, libonlp is the python library which internally define the function of ‘get_fans'.This function returns list of fan objects. In the loop above, all the fans rpm is being set to 10000 and all the fans description is being printed.


## License
