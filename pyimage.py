#!/usr/bin/python3
import time
import sys
import requests
from PIL import Image
try:
        file = sys.argv[1]
except:
        print("Bitte gebe einen Dateinamen oder einen link ein")
        exit()

try:
        imgsiz = sys.argv[2]
except:
        imgsiz = "1"
        print("keine Bildgröße angegeben 1 wird verwendet")

imgsiz = int(imgsiz)

        
if(file[0:4]=="http"):
        imagee = requests.get(file, allow_redirects=True)
        open('file.png', 'wb').write(imagee.content)
        file = "file.png"

try:
        img = Image.open(file)
except:
        print("Datei nicht gefunden")
        exit()
        
pixels = img.getdata()

def updatescreen():
	pygame.display.flip()
	
def clear():
	screen.fill(BLACK)
	
def pixel(pos, color):
	screen.fill(color, (pos, (1, 1)))

def main():
	for b in range(0, HEIGHT):
		updatescreen()
		for a in range(0, WIDTH):
			pixel((a, b), pixels[(a * round(imgsiz))+(((b *round(imgsiz)) * WIDTH) * round(imgsiz))])
	

import pygame
WIDTH, HEIGHT = img.size
WIDTH = round(WIDTH / imgsiz)
HEIGHT = round(HEIGHT / imgsiz)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyImage - " + file)
main()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	
pygame.quit()
