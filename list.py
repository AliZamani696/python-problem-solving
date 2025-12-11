
def checkSum(inList):
    newList = inList[0]
    total = 0
    ranges =inList[1:]
    for  i,x in ranges:
        total +=sum(newList[i:x])
        print(i,x)
    return total



mylist = [[1,2,3,4,4,5,6,7],[0,3],[1,4],[1,6],[2,4]]

print(checkSum((mylist)))
