class ParentClass:
    def __init__(self):
        self.__private_attribute = 0
        self._protected_attribute = 1
        self.public_attribute = 2

    def __private_method(self):
        print("ParentClass.__private_method() called")

    def _protected_method(self):
        print("ParentClass._protected_method() called")

    def public_method(self):
        print("ParentClass.public_method() called")

class ChildClass(ParentClass):  # Inherit from ParentClass
    def __init__(self):
        super().__init__()  # Call the parent class's initializer

    def __private_method(self):
        print("ChildClass.__private_method() called")

    def _protected_method(self):
        print("ChildClass._protected_method() called")

    def public_method(self):
        print("ChildClass.public_method() called")

def main():
    child = ChildClass()
    
    # Access public attribute and call public method
    print(child.public_attribute)
    child.public_method()

    # Call protected method
    child._protected_method()

    # Call parent's private method via name mangling
    child._ParentClass__private_method()

    # Call child's private method via name mangling
    child._ChildClass__private_method()

if __name__ == "__main__":
    main()
