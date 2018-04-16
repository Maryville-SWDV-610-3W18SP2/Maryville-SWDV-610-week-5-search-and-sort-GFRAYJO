def selectionSort(numList):
    for tableSlot in range(len(numList)-1,0,-1):
        maxPos = 0 
        for newPos in range(1,tableSlot+1):
            if numList[newPos]>numList[maxPos]:
                posMax = newPos
                
        tempSlot = numList[tableSlot]
        numList[tableSlot] = numList[maxPos]
        numList[maxPos] = tempSlot
        
    return numList

valList = [1,2,3,4,5,6,7,8,9,10]

selectionSort(valList)

print(selectionSort(valList))
