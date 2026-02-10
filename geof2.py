from struct import Struct

with open ('DATA/puzzle.data', 'rb') as read:
    data = read.read()
    #Create a Struct object with the correct format string
    s = Struct('f i f i f h H f I d f d I i I h')
    #Unpack the data using the Struct object
    unpackedData = s.unpack(data)
    resultStr = ""
    for num in unpackedData:
        i = (int)(num)
        print(chr(i), end="")
    print()
#        resultStr += chr(i)
#    print(resultStr)
     
    name = ''.join(chr(int(num)) for num in unpackedData)
    print(f"{name = }")
    