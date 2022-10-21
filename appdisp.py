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

cap = cv.VideoCapture(0)

print('Connetced camera')

while True:
    success, frame = cap.read()
    if success:
        frame = cv2.resize(frame, (320, 240), interpolation=cv2.INTER_AREA)
        img_tmp = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(img_tmp)
        image = image.rotate(90).resize((WIDTH, HEIGHT))
        disp.display(image)