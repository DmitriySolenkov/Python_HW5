def split(str):
    return [char for char in str]


def charCount(array, chr):
    count = 0
    for i in array:
        if i == chr:
            count += 1
    return count


def charComparison(array, chr):
    for i in array:
        if i == chr:
            return True
    return False


def charZip(charArray, countArray, index):
    if countArray[index] == 1:
        string = charArray[index]
    else:
        string = str(countArray[index])+charArray[index]
    return string


f = open('coding.txt', 'w')
f.write('AAAAABBBBCDEEEEEEEEFFFFFGGGGGHHHHHHIKKKKKPPPPPPPOOOQ')
f.close

f = open('coding.txt', 'r')
line = str(f.read())
f.close
lineArray = split(line)

charArray = []
countArray = []

for i in lineArray:
    if charComparison(charArray, i) == False:
        count = charCount(lineArray, i)
        charArray.append(i)
        countArray.append(count)

zipArray = []

for i in range(len(charArray)):
    zipArray.append(charZip(charArray, countArray, i))

zipString = ''.join(zipArray)
print(zipString)
f = open('coded.txt', 'w')
f.write(zipString)
f.close
