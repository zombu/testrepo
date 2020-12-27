import smbus
import time
 
#bus = smbus.SMBus(0) # Rev 1 Pi
bus = smbus.SMBus(1) # Rev 2 Pi
 
DEVICE = 0x20 # Device Adresse (A0-A2)
IODIRA = 0x00 # Pin Register fuer die Richtung
IODIRB = 0x01 # Pin Register fuer die Richtung
GPIOA = 0x12 # Register fuer Eingabe (GPA)
GPIOB = 0x15 # Register fuer Ausgabe (GPB)
 
# Definiere GPA Pin 7 als Input (10000000 = 0x80)
# Binaer: 0 bedeutet Output, 1 bedeutet Input
bus.write_byte_data(DEVICE,IODIRA,0x00)
 
# Definiere alle GPB Pins als Output (00000000 = 0x00)
bus.write_byte_data(DEVICE,IODIRB,0x00)
 
# Setze alle 7 Output bits auf 0
bus.write_byte_data(DEVICE,GPIOA,0)
bus.write_byte_data(DEVICE,GPIOB,0)
 
portA=0 
 
 # which=0..7
def onA(which):
    global portA
    bit=(1 << which)
    portA=portA | bit
    bus.write_byte_data(DEVICE,GPIOA,portA)
   
def offA(which):
    global portA
    bit=(1 << which)
    portA=portA & (~bit)
    bus.write_byte_data(DEVICE,GPIOB,portA)
 
for i in range(0,4):
  onA()
  time.sleep(0.5)
  offA()
  time.sleep(0.5)
