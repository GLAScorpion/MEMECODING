from logging import exception
import turtle
import mygui as ui

def main():
    d1 = data(True)
    d2 = data(False)
    d3 = data(True)
    d4 = data(False)
    gates = gatelist([d1,d2,d3,d4])
    print(gates.datalist)
    mk1 = nand(gates,[-1,-3])
    mk2 = nand(gates,[-2,-4])
    mk3 = nand(gates,[0,1])
    print(gates.nandlist)
    gates.additem(mk1)
    gates.additem(mk2)
    gates.additem(mk3)
    print(mk1.state + "\n" + mk2.state + "\n" + mk3.state)
    

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
            print(str(self.state) + " " + str(y))
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
            self.datalist.append(item)
        elif isinstance(item,nand):
            self.nandlist.append(item)
        else:
            raise TypeError("Incorrect data type in list")

    def getitem(self,item):
        if int(item)>=0:
            return self.nandlist[item]
        else:
            return self.datalist[-item-1]

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