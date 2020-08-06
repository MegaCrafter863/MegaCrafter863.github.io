from PIL import Image

#======================
file = "img.png"
sw =   128
#======================

hexb = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
binb = ["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]

img = Image.open(file)
imgpixels = img.getdata()
sizex, sizey = img.size

pixel = ""

def convert():
	global pixel
	for b in range(0, sizey):
		for a in range(0, sizex):
			if(imgpixels[(a)+(((b) * sizex))][0] + imgpixels[(a)+(((b) * sizex))][1] + imgpixels[(a)+(((b) * sizex))][2] / 3<=sw):
				pixel = pixel + "0"
			else:
                                if(imgpixels[(a)+(((b) * sizex))][0] + imgpixels[(a)+(((b) * sizex))][1] + imgpixels[(a)+(((b) * sizex))][2] / 3>=sw):
                                        pixel = pixel + "1"

#------------------------------------------------------------------------------------------------------------------------------------------------
def bin2hex(binn):
	global hexx
	hexx = ""
	for a in range(16):
		if(binn==binb[a]):
			hexx = hexb[a]
	return(hexx)

def main():
	convert()
	conpixel = []
	for a in range(round(len(pixel)/4)):
		conpixel = conpixel + [pixel[a*4:a*4+4]]

	global hexconpixel
	hexconpixel = []
	for a in conpixel:
		hexconpixel = hexconpixel + [bin2hex(a)]
		
	global fhexconpixel
	fhexconpixel = []
	for a in range(round(len(hexconpixel)/2)):
		fhexconpixel = fhexconpixel + ["0x" + hexconpixel[a*2] + hexconpixel[a*2+1]]

	return(fhexconpixel)
#-----------------------------------------------------------
out = ""
count = 0
for a in main():
	count = count + 1
	if(count>=round(sizex/8)):
		out = out + "\n"
		count = 1
	out = out + a + ", "
out = out[0:len(out)-2]
out = "HEIGHT: " + str(sizey) + "\nWIDTH: " + str(sizex) + "\n\n" + "static const unsigned char PROGMEM " + file + "[] = {\n" + out + " };"
f = open("img.h", "w")
f.write(out)
f.close()
