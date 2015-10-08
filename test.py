class Person():
    def __init__(self):
        self.foo = 'bar'

a_person = Person()
print(a_person.__class__.__name__)