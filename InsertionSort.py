def insertionSort(values):
    for i in range(1,len(values)):
        curNum = values[i]
        for n in range(i-1,0,-1):
            if values[n] > curNum:
                values[n+1] = values[n]
            else:
                values[n+1] = curNum
                break
                
newList = [2,5,7,1,3,9,4,10,6,8]

insertionSort(newList)

print(newList)              