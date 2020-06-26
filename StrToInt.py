# Guinea pig 1.0
# MIT License
# Allowed also as a commercial use, but only with crediting author, like "c MyTja Team"

def convert(lst): 
    res = sum(d * 10**i for i, d in enumerate(lst[::-1])) 
    return(res) 

def StrToInt(string):
    intcount = 0
    integers = []
    print(len(string))
    while (intcount < (len(string))):   #this is a loop
        i = string[intcount]
        # print(i) -- enable this for debugging
        if i=="1":
            integers.append(1)
        elif i=="2":
            integers.append(2)
        elif i=="3":
            integers.append(3)
        elif i=="4":
            integers.append(4)
        elif i=="5":
            integers.append(5)
        elif i=="6":
            integers.append(6)
        elif i=="7":
            integers.append(7)
        elif i=="8":
            integers.append(8)
        elif i=="9":
            integers.append(9)
        elif i=="0":
            integers.append(0)
        
        print(i)
        intcount = intcount + 1
    i = string.lower()
    if i=="zero":
        integers.append(0)
    elif string=="one":
        integers.append(1)
    elif string=="two":
        integers.append(2)
    elif string=="three":
        integers.append(3)
    elif string=="four":
        integers.append(4)
    elif string=="five":
        integers.append(5)
    elif string=="six":
        integers.append(6)
    elif string=="seven":
        integers.append(7)
    elif string=="eight":
        integers.append(8)
    elif string=="nine":
        integers.append(9)
    elif string=="ten":
        integers.append(10)
    else:
        return "This string contains unvalid symbols. Check if you have symbols or unvalid letters in string."
    intfinal = convert(integers)
    return intfinal
