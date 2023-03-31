message = 'a'


def greet(name):
    global message
    message = 'b'


greet("Nhat")
print(message)
