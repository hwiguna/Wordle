import machine
import ssd1306
import time

sclPIN = 33
sdaPIN = 34
oledWIDTH = 128
oledHEIGHT =  32

i2c = machine.SoftI2C( machine.Pin(sclPIN), machine.Pin(sdaPIN) )
oled = ssd1306.SSD1306_I2C( oledWIDTH, oledHEIGHT, i2c )
for i in range(1000,10000):
  oled.fill(0)
  oled.text('Static Text',0,0,1)
  oled.text(str(i),0,8,1)
  oled.text("label:"+str(10000-i),0,16,1)
  oled.show()
  time.sleep(.01)
