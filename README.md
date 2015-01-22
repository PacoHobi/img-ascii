img-ascii
=========

##Overview
img-ascii is a simple command-line utility that converts images to ASCII art images.

##Requirements
To run the img-ascii script you will need:
+ [Python 2.7](https://www.python.org/downloads/)
+ [Pillow](http://pillow.readthedocs.org/en/latest/installation.html)

##Usage
`python irc-ascii.pi input_file [options]`

###Options
Option     | Description
---------- | -----------
`-h`       | Show help text and exit
`-o file`  | Output file. Default is `output.png`
`-s w h`   | Width and height of output in characters
`-b float` | Brightness factor: `0.0` outputs solid black image, `1.0` outputs original brightness
`-c float` | Contrast factor: `0.0` outputs solid grey image, `1.0 outputs original contrast
`-i`       | Inverse black and white
