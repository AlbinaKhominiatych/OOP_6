class C:
    def __init__(self):
        print('c')

class A:
    def __init__(self):
        print('a')

class B(A):
    def __init__(self):
        super().__init__()
        print('b')

class D(B, A):
    def __init__(self):
        super().__init__()
        #A.__init__(self)
        print('d')

obj = D()