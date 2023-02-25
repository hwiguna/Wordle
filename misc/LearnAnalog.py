import machine
import time

hall = []

for i in range(2,6):
  temp = machine.ADC(machine.Pin(i))
  temp.atten(machine.ADC.ATTN_11DB)
  hall.append(temp)

while True:
    for i,x in enumerate(hall):
        a = x.read()
        print(i,a)
    time.sleep(1)
