import time

from time import gmtime, strftime
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

def led(n, block_orientation, rotate):
	serial = spi(port=0, device=0, gpio=noop())
	device = max7219(serial, cascaded=n or 1, block_orientation=block_orientation, rotate=rotate or 0)
	print("Created device")
	
	msg = strftime("%I:%M %P", localtime())
	print(msg)
	show_message(device, msg, fill="white", font=proportional(LCD_FONT))
	time.sleep(1)
	   
while True:
	led(4, -90, 0)
