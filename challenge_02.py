# We have a class defined for vehicles. Create two new vehicles called car1 and car 2. Set car1 to be a red convertible worth $60,000 with a name of Fer, and car3 to be a blue van named Jump worth $10,000.

class Car:
    def __init__(self,name,val,kind):
        self.val = val
        self.name = name
        self.kind = kind
    def printVal(self):
        print(self.val)
    def printName(self):
        print(self.name)
    def printKind(self):
        print(kind.self)

    def description(self):
        desc_str = "%s is a %s  worth $%s." % (self.name, self.kind, self.val)
        return desc_str

car1 = Car('Fer','60,000','red convertible')
car2 = Car('Jump','10,000', 'blue van')

print car1.description()
print car2.description()

car1.printVal()
