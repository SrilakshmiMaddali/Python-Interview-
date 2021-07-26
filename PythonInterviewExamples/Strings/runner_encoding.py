def encode_string(mystr):
    newstr=""
    if len(mystr) ==0 :
        return ""
    else:
        prevch=mystr[0]
        count=0
        for i in range(len(mystr)):
            if mystr[i]== prevch and i!=len(mystr):
                count+=1
            else:
                newstr+=str(count)+prevch
                prevch = mystr[i]
                count =1
            if i == len(mystr)-1:
                newstr += str(count) + prevch
    return newstr


print(encode_string("sssstttt"))

print(encode_string("aaaabbbbccccc"))