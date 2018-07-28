import time

from time import localtime, strftime
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

def led():
	serial = spi(port=0, device=0, gpio=noop())
	device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0)
	print("Device created")
	while True:
		msg = strftime("%H:%M%P", localtime())
		with canvas(device) as draw:
			text(draw, (0, 0), msg, fill="white", font=proportional(LCD_FONT))
	   
led()
