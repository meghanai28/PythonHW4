def allcaps (f):
    def inner():
        print(f().upper())
    return inner
