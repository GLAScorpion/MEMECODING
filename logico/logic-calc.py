import turtle

def main():
    prova = gate(tipo="nand" ,value=[True , True , True , True])
    print(prova.state)

class gate:
    def __init__(self,archive, tipo = "data", value = [False]):
        self.archive = archive
        self.items = value
        self.type = tipo
        self.state = True
        self.update()

    def update(self):
        if(self.type == "nand"):
            for x in self.items:
                #print(str(self.state) + " " + str(x))
                self.state = self.state and x
            self.state = not self.state

        else:
            self.state = self.items[0]

    #def link(self, newlink):


class gatelist:
    def __init__(self): 
        self.list = []
    def additem(self,item):
        self.list += item

if __name__ == "__main__":
	main()