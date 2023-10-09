def allcaps (f):
    def inner():
        str = f()
        str = str.upper
        print(str)
    return inner
