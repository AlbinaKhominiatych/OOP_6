#конспект
#множинне успадкування
class A:
    def say_hello(self):
        print("Hello from class A")
class B(A):
    def say_hello(self):
        print("Hello from class B")
class C(A):
    def say_hello(self):
        print("Hello from class C")
class D(C, B):
    pass
obj1 = A()
obj1.say_hello()
obj = D()
obj.say_hello()
print(D.mro())
print(D.__mro__)