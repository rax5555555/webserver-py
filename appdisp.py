from PIL import Image 
import cv2 
import ST7735 as TFT 
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI

WIDTH = 128
HEIGHT = 160
SPEED_HZ = 16000000
DC = 24
RST = 25
SPI_PORT = 0
SPI_DEVICE = 0

disp = TFT.ST7735(
    DC,
    rst=RST,
    spi=SPI.SpiDev(
        SPI_PORT,
        SPI_DEVICE,
        max_speed_hz=SPEED_HZ))

disp.begin()

cap = cv2.VideoCapture(0)

print('Connetced camera')

while True:
    success, frame = cap.read()
    if success:
       # frame = cv2.resize(frame, (320, 640), interpolation=cv2.INTER_AREA)
       # img_tmp = cv2.cvtColor(frame, cv2.COLOR_BGR2RBG)
        image = Image.fromarray(frame)
       # image = image.thumbnail((128,160))
        image = image.rotate(90)
        image = image.resize((217, 160))
       # image = image.rotate(90)
        image = image.crop((32,0,160,160))
        disp.display(image)
