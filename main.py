class UIElement:
    def __init__(self, name = "Hello"):
        self.name = name

    def display(self):
        pass


class InteractiveElement:
    def __init__(self, function="mega click"):
        self.function = function

    def click(self):
        pass


class Button(UIElement, InteractiveElement):
     def __init__(self):
         UIElement.__init__(self)
         InteractiveElement.__init__(self)


button = Button()  # Указываем значения для обоих родительских классов
print(button.name)
print(button.function)
button.display()