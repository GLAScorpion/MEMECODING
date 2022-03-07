import os
import argparse
import sys
import PIL
from PIL import Image
import sys
import math
import mygui
from mygui import MyGUIPage
from os import system
def rainbow(posix , offset):
	color = int ((posix % 1530) + offset)
	if color < 0:
		color = 1529 + color
	pos = int ((color % 1530) / 255)
	if pos == 0 :
		return (255, color % 255 , 0)	
	elif pos == 1:
		return (255 - (color % 255) , 255 , 0)
	elif pos == 2:
		return (0, 255 , color % 255)
	elif pos == 3:
		return (0, 255 - (color % 255) , 255)
	elif pos == 4:
		return (color % 255, 0 , 255)
	else:
		return (255, 0 , 255 - (color % 255))

def overwrite(item):
	files = os.listdir()
	for f in files:
		if f == item:
			os.remove(item)

def rainbowloop(image,size,output,diagonal,offset):
	loadedimage = image.load()
	for width in range(size[0]):
		for height in range(size[1]):
			if diagonal:
				offsetter = height
			else:
				offsetter = 0
			loadedimage[width , height] = rainbow(width, (offset-offsetter))
	image.close	
	overwrite(output)
	image.save(output)

def rainbow_converter(image,size,output,lumen,diagonal,offset):	
	rgb_image = image.convert("RGB")
	rgb_image.load()
	editimage = PIL.Image.new("RGB", size, color=0)
	loadedimage = editimage.load()
	for width in range(size[0]):
		for height in range(size[1]):
			if diagonal:
				offsetter = height
			else:
				offsetter = 0
			r , g , b = rgb_image.getpixel((width,height))
			r2 , g2 , b2 = rainbow(width, (offset-offsetter))
			r2 = r2 + r + lumen
			g2 = g2 + g + lumen
			b2 = b2 + b + lumen
			loadedimage[width , height] = ( r2 , g2 , b2 )
	rgb_image.close	
	editimage.close
	overwrite(output)
	editimage.save(output)

def file_list():
	page = MyGUIPage("File nella directory",20)
	direc = os.listdir()
	page.addstring(direc)
	page.printpage()
	choice = int(input("Scrivi il numero del file da elaborare\n"))
	return direc[choice - 1]
	
	
def main():	
	parser= argparse.ArgumentParser()
	parser.add_argument("--input", dest="input")
	parser.add_argument("--output", dest="output")
	parser.add_argument("--size", dest="size" , type = int , default = 1530)
	parser.add_argument("--lumen", dest="lumen" , type = int , default = 0)
	parser.add_argument("--offset", dest="offset" , type = int , default = 0)
	##parser.add_argument('-p', action='store', nargs='*') da usare con args.p != None
	parser.add_argument('--rainbow', action='store', nargs = '*')
	parser.add_argument('--gui', action='store', nargs = '*')
	args = parser.parse_args()
	if args.gui == None:
		size = (args.size , args.size)
		if args.input != None :
			image = PIL.Image.open(args.input)
			size = image.size ##(width,height)
		else:
			image = PIL.Image.new("RGB", size, color=0)		
			
		if (args.rainbow != None)and(args.input == None):
			rainbowloop(image , size , args.output)
		elif (args.rainbow !=None)and(args.input != None):
			image = PIL.ImageOps.grayscale(image)
			rainbow_converter(image , size , args.output, args.lumen,True,args.offset)
		else:
			image = PIL.ImageOps.grayscale(image)
			image.save(args.output)
	else:
		mainpage = MyGUIPage("Tool di editing grafico (ver 0.1)",20,"04")
		mainpage.addstring(("Genera una palette arcobaleno standard","Converti un'immagine in arcobaleno","Converti un'immagine in bianco e nero","Esci"))
		cicle = True
		wrongval = False
		while cicle:
			mainpage.printpage()
			if wrongval:
				print("Valore non valido. Riprova")
				wrongval = False
			choice = int(input("Scegli il numero corrispondente\n"))
			if choice == 1:
				secpage = MyGUIPage("Sezione palette arcobaleno standard",20)
				secpage.addstring(("Output: ","Dimensioni: ","Arcobaleno diagonale: ","Offset arcobaleno: "))	
				secpage.printpage()	
				imageoutput = input("Scrivi il nome del file da salvare\n")
				secpage.modstring(secpage.getstring(2) + imageoutput,2)	
				secpage.printpage()
				width = input("Inserisci la larghezza\n")
				ssize = width + "x" 
				secpage.modstring(secpage.getstring(3) + ssize,3)
				secpage.printpage()
				height = input("Inserisci l'altezza\n")
				secpage.modstring(secpage.getstring(3) + height,3)
				secpage.printpage()
				arcdiag=input("Disabilitare la stampa in diagonale dell'arcobaleno? (Y/N)\n")
				if arcdiag == "Y" or arcdiag == "y":
					secpage.modstring(secpage.getstring(4) + "False",4)
					arcdiagbool = False
				else:
					secpage.modstring(secpage.getstring(4) + "True",4)
					arcdiagbool = True
				secpage.printpage()
				offarc = input("Inserire un offset custom oppure lasciare vuoto\n")
				secpage.modstring(secpage.getstring(5) + offarc,5)
				secpage.printpage()
				if offarc == '':
					offarcval = 0
				else:
					offarcval = int(offarc)
				tmp = input("Procedere? (Y/N)\n")	
				if tmp == "Y" or tmp == "y":
					print("Elaborazione in corso...")
					size = (int(width),int(height))
					image = PIL.Image.new("RGB", size, color=0)
					rainbowloop(image,size,imageoutput,arcdiagbool,offarcval)
					print("Lavoro completato")
					system("pause")
			elif choice == 2:
				secpage = MyGUIPage("Sezione conversione immagine in arcobaleno",20)
				secpage.addstring(("Input: ","Output: ","Dimensioni: ","Offset luminosita': ","Arcobaleno diagonale: ","Offset arcobaleno: "))	
				imageinput = file_list()
				secpage.modstring(secpage.getstring(2) + imageinput,2)	
				secpage.printpage()
				image = PIL.Image.open(imageinput)
				size = image.size
				ssize = str(size[0]) + "x" + str(size[1])
				secpage.modstring(secpage.getstring(4) + ssize,4)
				secpage.printpage()
				imageoutput = input("Scrivi il nome del file da salvare\n")
				secpage.modstring(secpage.getstring(3) + imageoutput,3)	
				secpage.printpage()
				lumen = input("Inserisci un valore per cambiare la luminosità altrimenti lasciare vuoto\n")
				if lumen != '':
					secpage.modstring(secpage.getstring(5) + str(lumen),5)
					secpage.printpage()
					lumenvalue = int(lumen)
				else:
					lumen = str(0)
					secpage.modstring(secpage.getstring(5) + str(lumen),5)
					secpage.printpage()
					lumenvalue = int(lumen)
				arcdiag=input("Disabilitare la stampa in diagonale dell'arcobaleno? (Y/N)\n")
				if arcdiag == "Y" or arcdiag == "y":
					secpage.modstring(secpage.getstring(6) + "False",6)
					arcdiagbool = False
				else:
					secpage.modstring(secpage.getstring(6) + "True",6)
					arcdiagbool = True
				secpage.printpage()
				offarc = input("Inserire un offset custom oppure lasciare vuoto\n")
				secpage.modstring(secpage.getstring(7) + offarc,7)
				secpage.printpage()
				if offarc == '':
					offarcval = 0
				else:
					offarcval = int(offarc)
				tmp = input("Procedere? (Y/N)\n")	
				if tmp == "Y" or tmp == "y":
					print("Elaborazione in corso...")
					rainbow_converter(image,size,imageoutput,lumenvalue,arcdiagbool,offarcval)
					print("Lavoro completato")
					system("pause")
			
			elif choice == 3:
				secpage = MyGUIPage("Sezione grayscale",20)
				secpage.addstring(("Input: ","Output: ","Dimensioni: "))	
				imageinput = file_list()
				secpage.modstring(secpage.getstring(2) + imageinput,2)
				secpage.printpage()
				image = PIL.Image.open(imageinput)
				size = image.size
				ssize = str(size[0]) + "x" + str(size[1])
				secpage.modstring(secpage.getstring(4) + ssize,4)
				secpage.printpage()	
				imageoutput = input("Scrivi il nome del file da salvare\n")
				secpage.modstring(secpage.getstring(3) + imageoutput,3)	
				secpage.printpage()
				tmp = input("Procedere? (Y/N)\n")	
				if tmp == "Y" or tmp == "y":
					print("Elaborazione in corso...")
					image = PIL.ImageOps.grayscale(image)
					image.save(imageoutput)
					print("Lavoro completato")
					system("pause")
		
			elif choice == (mainpage.num - 3):
				cicle = False
				system("color 07")
				system("cls")
			else:
				wrongval = True
		
		
		
if __name__ == "__main__":
	sys.exit(main())
