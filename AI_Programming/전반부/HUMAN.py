class HUMAN:
    SECRETNUMBER = 486
    def __init__(self,num) :
        self._num = num
    # @classmethod -> classmethod 적용하면 h1에만 호출해도 h1, h2 다 적용 됨
    def do_something(self):
        self.SECRETNUMBER += 1

h1 = HUMAN(10)
h2 = HUMAN(20)

print(h1._num)
# HUMAN.SECRETNUMBER += 1
h1.do_something()
print(h1.SECRETNUMBER)
print('h2',h2.SECRETNUMBER)


