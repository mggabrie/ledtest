import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, TINY_FONT

def led():
	msg = input("Enter intensity 0-255: ")
	device.contrast(int(msg))
	with canvas(device) as draw:
		for i in range(4):
			text(draw, (0, 0), msg, fill="white", font=proportional(TINY_FONT))
			time.sleep(1)

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0)

while True:
	led()
