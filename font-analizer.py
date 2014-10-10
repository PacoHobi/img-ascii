from PIL import Image, ImageFont, ImageDraw

chars = []
intensity = []
for i in range(32,127):
	chars.append(chr(i))

fw = 8
fh = 8
font = ImageFont.load_default()
for char in chars:
	img = Image.new('L', (fw,fh), color=255)
	draw = ImageDraw.Draw(img)
	draw.text((0, -2), char, font=font)
	(w,h) = img.size
	c = 0
	for row in range(0,h):
		for col in range(0,w):
			if img.getpixel((col,row)) < 255:
				c += 1
	intensity.append((char,c))

intensity = [(b,a) for (a,b) in sorted([(b,a) for (a,b) in intensity])]

chars = []
last = -1
for (char,i) in intensity:
	if i is not last:
		chars.append(char)
		last = i

print ''.join(chars)