def split(str):
    return [char for char in str]


f = open('coded.txt', 'r')
zipString = f.read()
f.close
zipArray = split(zipString)
print(zipArray)
unzipArray = []
i = 0
while i <= len(zipArray)-1:
    if zipArray[i].isdigit():
        unzipArray.append(str(zipArray[i+1]*int(zipArray[i])))
        i += 2
    else:
        unzipArray.append(str(zipArray[i]))
        i += 1
unzipString = ''.join(unzipArray)
print(unzipString)

f = open('decoded.txt', 'w')
f.write(unzipString)
f.close
