from ctypes import *
class libonlp:
    def __init__(self):
        libonlp = CDLL('/lib/x86_64-linux-gnu/libonlp.so')  #Using ctypes to load "C" library.

        """
           Retrieve fan information
           Parameter 1(id): The fan OID
           Parameter 2(rv): Recieves fan information
        """
        libonlp.onlp_fan_info_get.argtypes = [onlp_oid_t, POINTER(onlp_fainfo_t)]
        libonlp.onlp_fan_info_get.restype = c_int

        #Initialize the fan subsystem
        libonlp.onlp_fan_init.argtypes =  [c_void]
        libonlp.onlp_fan_init.restype = c_int

        """
            Retrieve the fan's operational status.
            Paramenter 1(id): The fan OID.
            Parameter 2(rv) [out]: Receives the fan's operations status flags.
            Note: Only operational state needs to be returned - PRESENT/FAILED
        """
        onlp_fan_status_get.argtypes(onlp_oid_t,POINTER(c_uint))
        onlp_fan_status_get.restype(c_int)

        """
            Retrieve the fan's OID hdr
            Parameter 1(id): The Fan OID
            Parameter 2(rv) : Receives the OID header
        """
        onlp_fan_hdr_get.argtypes[onlp_oid_t,POINTER(onlp_oid_hdr_t)]
        onlp_fan_hdr_get.restype(c_int)

        """
            Set the fan speed in rpm
            Parameter 1(id):The fan OID
            Parameter 2(rpm): The new rpm
            Note: Only valid if the fan has teh SET_RPM capability
        """

        onlp_fan_rpm_set.argtypes[onlp_oid_t,c_ints]
        onlp_fan_rpm_set.restype = c_int

        """
             Set the fan speed in percentage.
             * @param id The fan OID.
             * @param p The percentage.
             * @note Only valid if the fan has the SET_PERCENTAGE capability.
        """
        onlp_fan_percentage_set.argtypes[onlp_oid_t,c_int]
        onlp_fan_percentage_set.restype = c_int

        """
            Set the fan by mode
            Parameter 1(id): The fan id
            Parameter 2(mode): The fan mode value
        """
        onlp_fan_mode_set.argtypes[onlp_oid_t,onlp_fan_mode_t]
        onlp_fan_mode_set.restype(c_int)

        """
            Set the fan direction
            Parameter 1(id): The fan OID
            Parameter 2(dir): The fan direction (B2F or F2B)
            Note: Only called if both capabilities are set
        """

        onlp_fan_dir_set.argtypes[onlp_oid_t,onlp_fan_dir_t]
        onlp_fan_dir_set.restype = c_int

        """
            Fan OID debug dump
            Parameter 1(id): The fan OID
            Parameter 2(pvs): The output pvs
            Parameter 3(flas): The output flags
        """

        onlp_fan_dump.argtypes[onlp_oid_t,POINTER(aim_pvs_t),c_uint]
        onlp_fan_dump.restype = c_void

        """
            Show the given Fan OID
            Parameter 1(id): The fan OID
            Parameter 2(pvs): The output pvs
            Parameter 3(flas): The output flags
        """
        onlp_fan_show.argtypes(onlp_oid_t,POINTER(aim_pvs_t),c_uint)
        onlp_fan_show.restype = c_void

        """
        Enum names
        """
        onlp_fan_caps_name.argtypes(onlp_fan_caps_t)
        onlp_fan_caps_name.restype = POINTER(c_char)

        """
        Enum values
        """
        onlp_fan_caps_value.argtypes(POINTER(c_char),POINTER(onlp_fan_caps_t),c_int)
        onlp_fan_caps_value.restype = c_int
