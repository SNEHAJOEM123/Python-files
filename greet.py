def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")
greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print("How do you do {name}?")
    print("Isn't the weather nice today?")
greet_with_name("Angela")    

def greet_with_more_parameters(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
greet_with_more_parameters("Jack Bauer","London")
greet_with_more_parameters(location="Korea",name="Ann")