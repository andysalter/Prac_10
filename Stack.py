"""
@author: Andrew Salter,Nathan Tse
@since: 11/09/2015
@modified: 15/09/2015
"""


class Stack:

    def __init__(self, size):
        """
        @description: checks if the size is positive and instantiates the stack
        @:param Size: the size of the list
        @:return: none
        @pre-conditions: none
        @post-conditions: self.the_array, self.count, self.top are initialised
        @Complexity: O(n)
        """
        assert type(size) is int
        assert size > 0, "size should be positive"
        self.the_array = size*[None]
        self.count = 0
        self.top = -1


    def __len__(self):
        """
        @description: has the value of the length of the stack
        @param: none
        @return: self.count which is the value of the length of the list
        @pre-conditions: an instance of Stack has been instantiated
        @post-conditions: None
        @Complexity: O(1)
        """
        return self.count

    def __str__(self):
        string = str()
        for _ in range(1, len(self) + 1):
            string = string + " " + str(self.peek(_))
        return string


    def is_empty(self):
        """
        @description: checks if the stack is empty
        @param: none
        @:return: True if length of the stack equal to zero, False otherwise
        @pre-conditions: an instance of Stack has been instantiated
        @post-conditions: None
        @Complexity: O(1)
        """
        return len(self) == 0


    def is_full(self):
        """
        @description: checks if the stack is full
        @param: none
        @return: length of the stack greater or equal to length of the array
        @pre-conditions: none
        @post-conditions: none
        @Complexity: O(1)
        """
        return len(self) >= len(self.the_array)


    def push(self, new_item):
        """
        @description: adds a new item on top of the stack
        @param: new_item: a value to be put into the stack
        @return: none
        @pre-conditions: Stack is not full
        @post-conditions: item is added to the stack, top is increased and count is increased
        @complexity: O(1)
        """
        assert not self.is_full(), "The stack is full."
        self.top += 1
        self.the_array[self.top] = new_item
        self.count += 1


    def pop(self):
        """
        @description: the item on top of the stack is taken off
        @param: none
        @return: none
        @preconditions: stack is not empty
        @post-conditions: item at the top of the stack is popped off, top is decreased and count is decreased
        @Complexity: O(1)
        """
        if self.is_empty():
            raise Exception("The stack is empty")
        item = self.the_array[self.top]
        self.top -= 1
        self.count -= 1
        return item


    def peek(self, index):
        assert not self.is_empty(), "The stack is empty"
        assert 0 < index < len(self) + 1, "Invalid index"
        index = (self.top - index) + 1
        item = self.the_array[index]
        return item
