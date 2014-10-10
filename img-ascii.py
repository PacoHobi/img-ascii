import sys
from PIL import Image, ImageEnhance, ImageFont, ImageDraw

def pixelValues(image):
	res = []
	(width, height) = image.size
	for row in range(0,height):
		for col in range(0,width):
			res.append(image.getpixel((col,row)))
	return res

def imageToAscii(image, chars):
	if verbose:
		print 'Trasforming pixels to ascii characters:'
	res = ''
	(width, height) = image.size
	totalPixels = width * height
	currentPixel = 0
	for row in range(0,height):
		for col in range(0,width):
			currentPixel += 1
			if verbose:
				printPercentage(currentPixel, totalPixels, 5)
			res = res + chars[image.getpixel((col,row))]
	if verbose:
		sys.stdout.write('\n')
	return res

def createAsciiImage(ascii,width,height):
	if verbose:
		print 'Trasforming ascii characters to image:'
	font = ImageFont.load_default()
	fw = 7
	fh = 7
	image = Image.new('L', (fw*width,fh*height), color=255)
	draw = ImageDraw.Draw(image)
	currentChar = 0
	for row in range (0,height):
		for col in range (0,width):
			currentChar += 1
			if verbose:
				printPercentage(currentChar, len(ascii), 5)
			draw.text((col*fw, row*fh), ascii[row*width+col], font=font)
	if verbose:
		sys.stdout.write('\n')
	return image

def limitToLevels(image, levels):
	p = 255/(levels-1)
	return img.point(lambda x: x/p, '1')	

def inverseColor(image):
	return img.point(lambda x: 255-x)

def adjustBrightness(image, brightness):
	return img.point(lambda x: brightness*x)

def printPercentage(current, total, step):
	perc = int(100.0*current/total)
	if perc%step is 0:
		sys.stdout.write('\r[%-20s] %3d%%' % ('='*(perc/5), perc))

def print_help():
	print 'Default output image format is PNG, it is recommended using PNG due to file size.\n'
	print 'usage: img-ascii.py input_file [options]'
	print 'Options:'
	print "-b float : brightness factor: 0.0 outputs solid black image, 1.0 outputs original brightness"
	print "-c float : contrast factor: 0.0 outputs solid grey image, 1.0 outputs original contrast"
	print "-i       : inverse black and white"
	print "-h       : show this help text and exit"
	print "-o file  : output file. Default: 'output.png'"
	print "-s w h   : width and height of output in characters"


verbose = True
inputFile = ''
width = 0
height = 0
brightness = -1
contrast = -1
inverse = False
output = 'output.png'
i = 1
if '-h' in sys.argv:
	print_help()
	sys.exit(0)
try:
	while i<len(sys.argv):
		arg = sys.argv[i]
		if arg == '-o':
			i += 1
			output = sys.argv[i]
		elif arg == '-b':
			i += 1
			brightness = float(sys.argv[i])
		elif arg == '-c':
			i += 1
			contrast = float(sys.argv[i])
		elif arg == '-i':
			i += 1
			inverse = True
		elif arg == '-s':
			i += 1
			width = int(sys.argv[i])
			i += 1
			height = int(sys.argv[i])
		elif arg[0] == '-':
			raise Exception(arg)
		elif inputFile == '':
			inputFile = sys.argv[i]
		else:
			raise Exception(arg)
		i += 1
except Exception as ex:
	print 'Error in input: %s\nusage: img-ascii.py input_file [options]\nTry \'img-ascii.py -h\' for more information.' %(ex)
	sys.exit(0)

chars = ' .,\'-"|/*!(vIJF7&%#A58$H'
try:
	img = Image.open(inputFile)
except:
	print('No such file: \'%s\'' %(inputFile))
if width is 0 or height is 0:
	(width, height) = img.size
img = img.convert(mode='L')
img = img.resize((width,height))
if brightness is not -1:
	img = ImageEnhance.Brightness(img).enhance(brightness)
if contrast is not -1:
	img = ImageEnhance.Contrast(img).enhance(contrast)
if not inverse:
	img = inverseColor(img)
img = limitToLevels(img, len(chars))
ascii = imageToAscii(img, chars)
asciiImage = createAsciiImage(ascii,width,height)
if verbose:
	print 'Saving image...'
asciiImage.save(output)
if verbose:
	print 'Finished'