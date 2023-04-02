class Stack():
    def __init__(self):
         self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def is_palindrome(s):
    stack = Stack()
    stack_reverse = ""
    for char in s:
        stack.push(char)
    while not stack.isEmpty():
        stack_reverse += stack.pop()
    return s == stack_reverse 

if __name__ == '__main__':
    print(is_palindrome("hello"))
    print(is_palindrome("madam"))   