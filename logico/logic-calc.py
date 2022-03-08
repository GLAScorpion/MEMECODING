from logging import exception
import turtle
import mygui as ui

def main():
    prova = nand(value=[True , True , True , True])
    print(prova.state)

class data:
    num = -1

    def __init__(self, state = True):
        self.state = state
        self.num = data.num
        data.num -= 1
    
    def dynstate(self):
        return self.state
        
class nand:
    num = 0

    def __init__(self,archive, items):
        self.archive = archive
        self.items = items
        self.state = True
        self.num = nand.num
        nand.num += 1
        self.update()

    def update(self):
        for y in self.items:
            #print(str(self.state) + " " + str(x))
            x = self.archive.getitem(y)
            self.state = self.state and x.dynstate()
        self.state = not self.state

    def dynstate(self):
        self.update()
        return self.state
    
    def newlink(self, newlink):
        self.items += newlink
        self.update()

class gatelist:
    def __init__(self, items = []): 
        self.datalist = []
        self.nandlist = []
        for x in items:
            self.additem(x)

    def additem(self,item):
        if isinstance(item,data):
            self.datalist += item
        elif isinstance(item,nand):
            self.nandlist += item
        else:
            raise TypeError("Incorrect data type in list")

    def getitem(self,item):
        if item>=0:
            return self.archive.nandlist[item]
        else:
            return self.archive.datalist[-item-1]

    def removeitem(self,item):
        if isinstance(item,(data,nand)):
            val = item.num
            obj = item
        elif isinstance(item,int):
            obj = self.getitem(item)
            val = item
        else:
            raise TypeError("Invalid object")
        if isinstance(item,data):
            self.datalist.remove(obj)
        elif isinstance(item,nand):
            self.nandlist.remove(obj)
        for x in self.nandlist:
            x.items.remove(val)
        self.nandlist[len(self.nandlist)-1].dynupdate()

if __name__ == "__main__":
	main()