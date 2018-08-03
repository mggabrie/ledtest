import time
import bs4
import urllib.request

from time import localtime, strftime
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, TINY_FONT

def led():
	msg = strftime("%I:%M%p", localtime())
	with canvas(device) as draw:
		text(draw, (0, 0), msg, fill="white", font=proportional(TINY_FONT))
def temp():
	url = "https://weather.com/weather/today/l/10461:4:US"
	html = urllib.request.urlopen(url)
	soup_html = bs4.BeautifulSoup(html, "html.parser")
	temp_html = soup_html.find("div", attrs={"class": "today_nowcard-temp"})
	temp_msg = temp_html.text.strip()
	hum_html = soup_html.find("div", attrs={"class": "today_nowcard-sidecar component panel"})
	hum_msg = hum_html.text.strip()
	i = hum_msg.find("Humidity")
	with canvas(device) as draw:
		text(draw, (0, 0), (temp_msg[0:2]+"F "+hum_msg[i+8:i+11]), fill="white", font=proportional(TINY_FONT))
	time.sleep(3)
	phrase_html = soup_html.find("div", attrs={"class": "today_nowcard-phrase"})
	phrase_msg = phrase_html.text.strip()
	println(device, phrase_msg, fill="white", font=proportional(TINY_FONT))
		
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0)
device.contrast(10)

while True:
	for i in range(2):
		led()
		time.sleep(1)
	try:
		temp()
	except:
		continue
