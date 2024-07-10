class MathList:
    def _innit_(seft,values) -> None :
        self.values = values
        self.length = len(values)

    def _str_(seft) -> str:
        return str(self.values)

    def _add_(seft,num):
        for i in range(len(self.values)):
            self.values[i] += num
        return self

     def _sub_(seft,num):
        for i in range(len(self.values)):
            self.values[i] -= num
        return self
list_a = MathList([1,2,3])
print(list_a)
list_a = MathList([1,2,3])
print(list_a)