def allcaps (f):
    def inner():
        print(f().lower())
   
    return inner
