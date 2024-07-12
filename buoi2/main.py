class Parent:
    def _init_(self,name) :
        self.name = name

    #overriding
    def _str_(self) -> str:
        return self.name
#init obj ( parent type )
obj = Parent("ABC")
print(obj._str_())

class Sub(Parent):
    def _init_(self,name,age):
        supper()._init_(name)
        self.age = age

    def _str_(self) -> str:
        return supper()._str_() + "," + str(self.age)
    
obj2 = Sub("ABCD",2)
print(obj2._str_())