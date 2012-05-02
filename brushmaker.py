
from math import *
import png

def make_brush(radial_function, sidelength, filename):
	flat_pixels = []
	halflength = 0.5 * sidelength
	for x in range(sidelength):
		for y in range(sidelength):
			r = sqrt((x + 0.5 - halflength) ** 2 + (y + 0.5 - halflength) ** 2) / halflength
			a = int(round(255 * radial_function(r)))
			if a < 0:
				a = 0
			if 255 < a:
			 	a = 255
			flat_pixels += [255, 255, 255, a]
	f = open(filename, 'wb')
	w = png.Writer(width=sidelength, height=sidelength, alpha=True)
	w.write_array(f, flat_pixels)
	f.close()

if __name__ == '__main__':
	make_brush(lambda r : 1.0 - r, 64, 'testbrush.png')
