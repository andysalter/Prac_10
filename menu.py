
class Menu:
    def __init__(self, prompt, option_list=[]):
        assert type(option_list) is list, "Options must be in a list"
        self.options = option_list
        self.prompt = '\n' + prompt + '\n\n'

    def __str__(self):
        string = self.prompt
        options = list(enumerate(self.options))
        for count, operation in options:
            string += str(count + 1) + ". " + str(operation) + "\n"
        return string

    def __repr__(self):
        return self.options

    def __iter__(self):
        return enumerate(self.options)

    def __len__(self):
        return len(self.options)

    def insert(self, index, item):
        self.options.insert(index, item)

    def remove(self, option):
        self.options.remove(option)

    def select(self, selection):
        selection = int(selection)
        selection -= 1
        menu = dict(self)
        if selection not in menu:
            raise IndexError("Selection not in menu")
        return menu[selection]