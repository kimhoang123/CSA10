class Animal:
    # memmber variable - attribute(dung de mieu ta)
    name = "abc"
    age = 0.5
    # ham khoi tao( phuwong thuc dung de hoat dong)
    def _init_(self,name):
        self.name = name
        #pass
    #method - phuong thuc
    def talk() :
        print("talk")
cuu = Animal(name = "xyz")
soi = Animal(name = "xyz")
print(cuu.name)#xyz , co pass => abc
cuu.talk()
