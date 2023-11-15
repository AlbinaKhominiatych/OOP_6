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
    def say_hello(self):
        super().say_hello()
        A.say_hello(self)
        
obj = D()
obj.say_hello()
print(D.mro())
print(D.__mro__)