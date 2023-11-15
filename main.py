class C:
    def __init__(self):
        print('c')

class A:
    def __init__(self):
        print('a')

class B(C):
    def __init__(self):
        C.__init__(self)
        print('b')

class D(B, A):
    x = 'X'