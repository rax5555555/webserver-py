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
disp.clean()

cap = cv2.VideoCapture(0)

print('Connetced camera')

while True:
    success, frame = cap.read()
    if success:
        frame = cv2.rotate(90).resize(frame, (217, 160), interpolation=cv2.INTER_AREA)
        img_tmp = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(img_tmp, cv2.COLOR_RGB2GRAY)
        _, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
        
        #img_tmp = cv2.cvtColor(frame, cv2.COLOR_RBG2BGR)
        image = Image.fromarray(binary)
        #image = image.rotate(90)
        #image = image.resize((217, 160))
        image = image.crop((32,0,160,160))
        disp.display(image)
