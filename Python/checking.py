def display(a,*args, **kwargs):
    print("a:",a)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Calling with both positional and keyword arguments
display(1, 2, 3, name="Alice", age=30)