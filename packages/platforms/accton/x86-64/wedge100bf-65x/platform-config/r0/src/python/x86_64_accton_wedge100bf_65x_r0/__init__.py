from onl.platform.base import *
from onl.platform.accton import *

class OnlPlatform_x86_64_accton_wedge100bf_65x_r0(OnlPlatformAccton,
                                                OnlPlatformPortConfig_64x100):
    MODEL="Wedge-100bf-65x"
    PLATFORM="x86-64-accton-wedge100bf-65x-r0"
    SYS_OBJECT_ID=".100.65.1"

    def baseconfig(self):
        self.insmod('optoe')
        
        ########### initialize I2C bus 1 & bus 2 ###########
        self.new_i2c_devices([
         # initialize multiplexer (PCA9548)
                ('pca9548', 0x70, 1),
                ('pca9548', 0x71, 1),
                ('pca9548', 0x72, 1),
                ('pca9548', 0x73, 1),
                ('pca9548', 0x74, 1),


                # initialize multiplexer (PCA9548)
                ('pca9548', 0x70, 2),
                ('pca9548', 0x71, 2),
                ('pca9548', 0x72, 2),
                ('pca9548', 0x73, 2),
                ('pca9548', 0x74, 2),

                ('24c64', 0x50, 41),
                ])
                
        # Initialize QSFP devices
        self.new_i2c_device('optoe1', 0x50, 3)
        self.new_i2c_device('optoe1', 0x50, 4)
        self.new_i2c_device('optoe1', 0x50, 5)
        self.new_i2c_device('optoe1', 0x50, 6)
        self.new_i2c_device('optoe1', 0x50, 7)
        self.new_i2c_device('optoe1', 0x50, 8)
        self.new_i2c_device('optoe1', 0x50, 9)
        self.new_i2c_device('optoe1', 0x50, 10)
        self.new_i2c_device('optoe1', 0x50, 11)
        self.new_i2c_device('optoe1', 0x50, 12)
        self.new_i2c_device('optoe1', 0x50, 13)
        self.new_i2c_device('optoe1', 0x50, 14)
        self.new_i2c_device('optoe1', 0x50, 15)
        self.new_i2c_device('optoe1', 0x50, 16)
        self.new_i2c_device('optoe1', 0x50, 17)
        self.new_i2c_device('optoe1', 0x50, 18)
        self.new_i2c_device('optoe1', 0x50, 19)
        self.new_i2c_device('optoe1', 0x50, 20)
        self.new_i2c_device('optoe1', 0x50, 21)
        self.new_i2c_device('optoe1', 0x50, 22)
        self.new_i2c_device('optoe1', 0x50, 23)
        self.new_i2c_device('optoe1', 0x50, 24)
        self.new_i2c_device('optoe1', 0x50, 25)
        self.new_i2c_device('optoe1', 0x50, 26)
        self.new_i2c_device('optoe1', 0x50, 27)
        self.new_i2c_device('optoe1', 0x50, 28)
        self.new_i2c_device('optoe1', 0x50, 29)
        self.new_i2c_device('optoe1', 0x50, 30)
        self.new_i2c_device('optoe1', 0x50, 31)
        self.new_i2c_device('optoe1', 0x50, 32)
        self.new_i2c_device('optoe1', 0x50, 33)
        self.new_i2c_device('optoe1', 0x50, 34)
        self.new_i2c_device('optoe1', 0x50, 43)
        self.new_i2c_device('optoe1', 0x50, 44)
        self.new_i2c_device('optoe1', 0x50, 45)
        self.new_i2c_device('optoe1', 0x50, 46)
        self.new_i2c_device('optoe1', 0x50, 47)
        self.new_i2c_device('optoe1', 0x50, 48)
        self.new_i2c_device('optoe1', 0x50, 49)
        self.new_i2c_device('optoe1', 0x50, 50)
        self.new_i2c_device('optoe1', 0x50, 51)
        self.new_i2c_device('optoe1', 0x50, 52)
        self.new_i2c_device('optoe1', 0x50, 53)
        self.new_i2c_device('optoe1', 0x50, 54)
        self.new_i2c_device('optoe1', 0x50, 55)
        self.new_i2c_device('optoe1', 0x50, 56)
        self.new_i2c_device('optoe1', 0x50, 57)
        self.new_i2c_device('optoe1', 0x50, 58)
        self.new_i2c_device('optoe1', 0x50, 59)
        self.new_i2c_device('optoe1', 0x50, 60)
        self.new_i2c_device('optoe1', 0x50, 61)
        self.new_i2c_device('optoe1', 0x50, 62)
        self.new_i2c_device('optoe1', 0x50, 63)
        self.new_i2c_device('optoe1', 0x50, 64)
        self.new_i2c_device('optoe1', 0x50, 65)
        self.new_i2c_device('optoe1', 0x50, 66)
        self.new_i2c_device('optoe1', 0x50, 67)
        self.new_i2c_device('optoe1', 0x50, 68)
        self.new_i2c_device('optoe1', 0x50, 69)
        self.new_i2c_device('optoe1', 0x50, 70)
        self.new_i2c_device('optoe1', 0x50, 71)
        self.new_i2c_device('optoe1', 0x50, 72)
        self.new_i2c_device('optoe1', 0x50, 73)
        self.new_i2c_device('optoe1', 0x50, 74)
        subprocess.call('echo port1 > /sys/bus/i2c/devices/44-0050/port_name', shell=True)
        subprocess.call('echo port2 > /sys/bus/i2c/devices/43-0050/port_name', shell=True)
        subprocess.call('echo port3 > /sys/bus/i2c/devices/46-0050/port_name', shell=True)
        subprocess.call('echo port4 > /sys/bus/i2c/devices/45-0050/port_name', shell=True)
        subprocess.call('echo port5 > /sys/bus/i2c/devices/48-0050/port_name', shell=True)
        subprocess.call('echo port6 > /sys/bus/i2c/devices/47-0050/port_name', shell=True)
        subprocess.call('echo port7 > /sys/bus/i2c/devices/50-0050/port_name', shell=True)
        subprocess.call('echo port8 > /sys/bus/i2c/devices/49-0050/port_name', shell=True)
        subprocess.call('echo port9 > /sys/bus/i2c/devices/52-0050/port_name', shell=True)
        subprocess.call('echo port10 > /sys/bus/i2c/devices/51-0050/port_name', shell=True)
        subprocess.call('echo port11 > /sys/bus/i2c/devices/54-0050/port_name', shell=True)
        subprocess.call('echo port12 > /sys/bus/i2c/devices/53-0050/port_name', shell=True)
        subprocess.call('echo port13 > /sys/bus/i2c/devices/56-0050/port_name', shell=True)
        subprocess.call('echo port14 > /sys/bus/i2c/devices/55-0050/port_name', shell=True)
        subprocess.call('echo port15 > /sys/bus/i2c/devices/58-0050/port_name', shell=True)
        subprocess.call('echo port16 > /sys/bus/i2c/devices/57-0050/port_name', shell=True)
        subprocess.call('echo port17 > /sys/bus/i2c/devices/60-0050/port_name', shell=True)
        subprocess.call('echo port18 > /sys/bus/i2c/devices/59-0050/port_name', shell=True)
        subprocess.call('echo port19 > /sys/bus/i2c/devices/62-0050/port_name', shell=True)
        subprocess.call('echo port20 > /sys/bus/i2c/devices/61-0050/port_name', shell=True)
        subprocess.call('echo port21 > /sys/bus/i2c/devices/64-0050/port_name', shell=True)
        subprocess.call('echo port22 > /sys/bus/i2c/devices/63-0050/port_name', shell=True)
        subprocess.call('echo port23 > /sys/bus/i2c/devices/66-0050/port_name', shell=True)
        subprocess.call('echo port24 > /sys/bus/i2c/devices/65-0050/port_name', shell=True)
        subprocess.call('echo port25 > /sys/bus/i2c/devices/68-0050/port_name', shell=True)
        subprocess.call('echo port26 > /sys/bus/i2c/devices/67-0050/port_name', shell=True)
        subprocess.call('echo port27 > /sys/bus/i2c/devices/70-0050/port_name', shell=True)
        subprocess.call('echo port28 > /sys/bus/i2c/devices/69-0050/port_name', shell=True)
        subprocess.call('echo port29 > /sys/bus/i2c/devices/72-0050/port_name', shell=True)
        subprocess.call('echo port30 > /sys/bus/i2c/devices/71-0050/port_name', shell=True)
        subprocess.call('echo port31 > /sys/bus/i2c/devices/74-0050/port_name', shell=True)
        subprocess.call('echo port32 > /sys/bus/i2c/devices/73-0050/port_name', shell=True)
        subprocess.call('echo port33 > /sys/bus/i2c/devices/4-0050/port_name', shell=True)
        subprocess.call('echo port34 > /sys/bus/i2c/devices/3-0050/port_name', shell=True)
        subprocess.call('echo port35 > /sys/bus/i2c/devices/6-0050/port_name', shell=True)
        subprocess.call('echo port36 > /sys/bus/i2c/devices/5-0050/port_name', shell=True)
        subprocess.call('echo port37 > /sys/bus/i2c/devices/8-0050/port_name', shell=True)
        subprocess.call('echo port38 > /sys/bus/i2c/devices/7-0050/port_name', shell=True)
        subprocess.call('echo port39 > /sys/bus/i2c/devices/10-0050/port_name', shell=True)
        subprocess.call('echo port40 > /sys/bus/i2c/devices/9-0050/port_name', shell=True)
        subprocess.call('echo port41 > /sys/bus/i2c/devices/12-0050/port_name', shell=True)
        subprocess.call('echo port42 > /sys/bus/i2c/devices/11-0050/port_name', shell=True)
        subprocess.call('echo port43 > /sys/bus/i2c/devices/14-0050/port_name', shell=True)
        subprocess.call('echo port44 > /sys/bus/i2c/devices/13-0050/port_name', shell=True)
        subprocess.call('echo port45 > /sys/bus/i2c/devices/16-0050/port_name', shell=True)
        subprocess.call('echo port46 > /sys/bus/i2c/devices/15-0050/port_name', shell=True)
        subprocess.call('echo port47 > /sys/bus/i2c/devices/18-0050/port_name', shell=True)
        subprocess.call('echo port48 > /sys/bus/i2c/devices/17-0050/port_name', shell=True)
        subprocess.call('echo port49 > /sys/bus/i2c/devices/20-0050/port_name', shell=True)
        subprocess.call('echo port50 > /sys/bus/i2c/devices/19-0050/port_name', shell=True)
        subprocess.call('echo port51 > /sys/bus/i2c/devices/22-0050/port_name', shell=True)
        subprocess.call('echo port52 > /sys/bus/i2c/devices/21-0050/port_name', shell=True)
        subprocess.call('echo port53 > /sys/bus/i2c/devices/24-0050/port_name', shell=True)
        subprocess.call('echo port54 > /sys/bus/i2c/devices/23-0050/port_name', shell=True)
        subprocess.call('echo port55 > /sys/bus/i2c/devices/26-0050/port_name', shell=True)
        subprocess.call('echo port56 > /sys/bus/i2c/devices/25-0050/port_name', shell=True)
        subprocess.call('echo port57 > /sys/bus/i2c/devices/28-0050/port_name', shell=True)
        subprocess.call('echo port58 > /sys/bus/i2c/devices/27-0050/port_name', shell=True)
        subprocess.call('echo port59 > /sys/bus/i2c/devices/30-0050/port_name', shell=True)
        subprocess.call('echo port60 > /sys/bus/i2c/devices/29-0050/port_name', shell=True)
        subprocess.call('echo port61 > /sys/bus/i2c/devices/32-0050/port_name', shell=True)
        subprocess.call('echo port62 > /sys/bus/i2c/devices/31-0050/port_name', shell=True)
        subprocess.call('echo port63 > /sys/bus/i2c/devices/34-0050/port_name', shell=True)
        subprocess.call('echo port64 > /sys/bus/i2c/devices/33-0050/port_name', shell=True)
        subprocess.call('ifconfig usb0 up', shell=True)

        return True