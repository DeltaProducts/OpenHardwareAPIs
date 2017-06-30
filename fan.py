from ctypes import *
from enum import Enum
import libonlp


#include the oids.py and 0nlp.py

class onlp_fan_caps_e(Enum):
    ONLP_FAN_CAPS_B2F = (1 << 0)
    ONLP_FAN_CAPS_F2B = (1 << 1)
    ONLP_FAN_CAPS_SET_RPM = (1 << 2)
    ONLP_FAN_CAPS_SET_PERCENTAGE = (1 << 3)
    ONLP_FAN_CAPS_GET_RPM = (1 << 4)
    ONLP_FAN_CAPS_GET_PERCENTAGE = (1 << 5)

#InitVal = onlp_fan_caps_e(1<<0,1<<1,1<<2,1<<3,1<<4,1<<5)
#print InitVal.ONLP_FAN_CAPS_GET_PERCENTAGE

#onlp_fan_dir
class onlp_fan_dir_e(Enum):   
    ONLP_FAN_DIR_B2F = ''
    ONLP_FAN_DIR_F2B = ''
    ONLP_FAN_DIR_LAST = ONLP_FAN_DIR_F2B
    ONLP_FAN_DIR_COUNT = ''
    ONLP_FAN_DIR_INVALID = -1


#onlp_fan_mode
class onlp_fan_mode_e(Enum):
    ONLP_FAN_MODE_OFF = ''
    ONLP_FAN_MODE_SLOW = ''
    ONLP_FAN_MODE_NORMAL = ''
    ONLP_FAN_MODE_FAST = ''
    ONLP_FAN_MODE_MAX = ''
    ONLP_FAN_MODE_LAST = ONLP_FAN_MODE_MAX
    ONLP_FAN_MODE_COUNT = ''
    ONLP_FAN_MODE_INVALID = -1

#onlp_fan_status
class onlp_fan_status_e(Enum):
    ONLP_FAN_STATUS_PRESENT = (1 << 0)
    ONLP_FAN_STATUS_FAILED = (1 << 1)
    ONLP_FAN_STATUS_B2F = (1 << 2)
    ONLP_FAN_STATUS_F2B = (1 << 3)

#Fan Information Structure
class onlp_fan_info_s(Structure):
    _fields_ = [
        #("hdr", onlp_oid_hdr_t),
        ("status", c_uint),
        ("caps", c_uint),
        ("rpm", c_int),
        ("percentage", c_int), #should it be float?
        ("mode", c_int),
        ("model", c_char * 64),    #model[ONLP_CONFIG_INFO_STR_MAX]
        ("serial",c_char * 64)   #serial[ONLP_CONFIG_INFO_STR_MAX]
        ]
