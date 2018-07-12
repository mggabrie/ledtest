from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial
                 
font = ImageFont.truetype("examples/pixelmix.ttf", 8)

with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
                 
from luma.core import legacy
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT

with canvas(device) as draw:
   legacy.text(draw, (0, 0), "A", fill="white", font=proportional(CP437_FONT))
