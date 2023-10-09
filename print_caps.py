def allcaps (f):
    def inner():
        val = f()
        if(isinstance(val,list)):
            for i in range(len(val)):
                if(isinstance(val[i],str)):
                    val[i] = val[i].upper()
            print(" ".join(val))
        if(isinstance(val,str)):
            print(val.upper())
   
    return inner
