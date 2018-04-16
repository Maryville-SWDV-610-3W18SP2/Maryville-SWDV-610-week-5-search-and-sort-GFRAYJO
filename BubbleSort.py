def bubbleSort(myList):
    for num in range(len(myList)-1,0,-1):
        for i in range(num):
            if myList[i]>myList[i+1]:
                placement = myList[i]
                myList[i] = myList[i+1]
                myList[i+1] = placement
                
    return myList
                

theValList = [2,5,7,1,3,9,4,10,6,8]

bubbleSort(theValList)

print(bubbleSort(theValList))
                
                
            