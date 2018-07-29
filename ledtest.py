import time

from time import localtime, strftime
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

def led():
	msg = strftime("%I:%M%P", localtime())
	with canvas(device) as draw:
		text(draw, (0, 0), msg, fill="white", font=proportional(LCD_FONT))
def temp():
	msg = "Readout"
	with canvas(device) as draw:
		text(draw, (0, 0), msg, fill="white", font=proportional(LCD_FONT))

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0)
device.contrast(40)

while True:
	for i in range(10):
		led()
		time.sleep(1)
	temp()
	time.sleep(10)
