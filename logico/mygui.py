from os import system
import math
def printastline(n):
	for x in range(n + 4):
		print("*",end='', flush=True)
	print()

def printstringast(string , n , index):
	print("*",end='', flush=True)
	l2 = int((n - len(string))/2)
	if (index-2) > 0:
		l1 = l2 + ((n - len(string))%2) - int(math.log10(index - 2))
	else:
		l1 = l2 + ((n - len(string))%2)
	for x in range(l1):
		print(" ",end='', flush=True)
	if index > 2:
		print(index-2,end='', flush=True)
		print("-" + string,end='', flush=True)
	else:
		print("  " + string,end='', flush=True)
	for x in range(l2):
		print(" ",end='', flush=True)
	print("*")
	
class MyGUIPage:
	def __init__(self , title, spacing = 6, color = "0A"):
		self.spacing = spacing
		self.color = "color " + color
		self.barlen = len(title) + self.spacing
		self.num = 3
		self.stringarray = [title , ""]
	
	def addstring(self,string):
		for x in string:
			self.num = self.num + 1
			if self.barlen <= len(x):
				self.barlen = len(x) + self.spacing
			self.stringarray.append(x)
		
	def printpage(self):
		system('cls')
		system(self.color)
		printastline(self.barlen)
		for x in range(1,self.num):
			printstringast(self.stringarray[x-1],self.barlen,x)
		printastline(self.barlen)	
	
	def getstring(self, index):
		return self.stringarray[index]
	
	def modstring(self,string,index):
		self.stringarray[index] = string
		if self.barlen <= len(string):
			self.barlen = len(string) + self.spacing
			
		
class MyGUIMenu:
	def __init__(self):
		self.pageslist = []
		self.pages = 0
		self.pagesnames = []
		
	def addpage(self , page, namepage):
		self.pagesnames.append(namepage)
		self.pageslist.append(page)
		self.pages = self.pages + 1
	
	def printmenupage(self, name):
		index = self.pagesnames.index(name)
		self.pageslist[index].printpage()
	

def main():##test
	menu = MyGUIMenu()
	mainmenu = MyGUIPage("Pagina principale")
	mainmenu.addstring("Pagina secondaria")
	mainmenu.addstring("Pagina Terziaria")
	menu.addpage(mainmenu,"main")
	secondmenu = MyGUIPage("Pagina secondaria")
	secondmenu.addstring("robba")
	secondmenu.addstring("robba")
	menu.addpage(secondmenu,"second")
	thirdmenu = MyGUIPage("Pagina terziaria")
	thirdmenu.addstring("robba")
	thirdmenu.addstring("robba")
	menu.addpage(thirdmenu,"third")
	while True:
		choice = int(input("Che pagina visualizzo?"))
		menu.printmenupage(choice)
	
if __name__ == "__main__":
	main()
