import machine
from machine import I2C
import vcnl4010
  
i2c = I2C(scl=machine.Pin(21),sda=machine.Pin(22))

vcnl = VCNL4010(i2c)
vcnl.startup()

for i in range(100):
  print("Ambient:", vcnl.readAmbientLux() * VCNL4010_AMBIENT_LUX_SCALE, "lux")
  print("Proximity:", vcnl.readProximity() * 256 / 65555)