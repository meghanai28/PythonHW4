def allcaps (f):
    def inner():
        list = f().split()
        for i in range(len(list)):
            list[i] = list[i].upper()
        str = " ".join(list)
        print(str)
    return inner
