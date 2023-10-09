def allcaps (f):
    def inner():
        val = f()
        if(isinstance(val,str)):
            print(val.upper())
        if(isinstance(val,list)):
            for i in range(len(val)):
                if(isinstance(val[i],str)):
                    val[i] = val[i].upper()
            print(val)
   
    return inner
