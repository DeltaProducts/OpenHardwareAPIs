class libonlp:
    def __init__():
          libonlp = ctypes.CDLL('/lib/x86_64-linux-gnu/libonlp.so') // Using ctypes to load "C" library.
          libonlp.onlp_fan_info_get.argtypes = [ctypes.c_uint, ctypes.POINTER(onlp_fainfo_t)] // Sample prototype of the "C" function.
          libonlp.onlp_fan_info_get.restype = ctypes.c_int
          .....//leds/sfp/psus e.t.c "C" prototypes will go here.
          
class onlp_fan_info_t(ctypes.Structure): // Similar structures need to be defined for other onlp supported components.
   _fields_ = [("hdr", onlp_oid_hdr),
              ("status", ctypes.c_uint),
              ("caps", ctypes.c_uint),
              ("rpm", ctypes.c_int),
              ("percentage", ctypes.c_int),
              ("mode", ctypes.c_int),
              ("model", ctypes.c_char * 64),
              ("serial",ctypes.c_char * 64)]   
              
//Following is Sample code for fan object. The sample test code written above uses the following functions.              
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