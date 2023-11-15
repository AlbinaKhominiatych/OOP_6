"""В данном коде строка super(C, self).
stop() используется для вызова метода stop из класса,
от которого был унаследован класс C. В данном случае,
класс C унаследован от класса A.
Итак, строка super(C, self).stop():
C - указывает, что мы ищем метод в иерархии наследования начиная с класса C.
self - передает текущий экземпляр класса C в метод.
Таким образом, super(C, self).stop() вызывает метод stop из класса,
от которого унаследован класс C, который в данном случае - это класс A."""
class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).stop()
        print("go B go!")


class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")


class E(B,C):
    pass

e=E()
e.go()