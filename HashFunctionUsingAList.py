class hashList:
    def __init__(self):
        self.size = 6
        self.famStrName = [None] * self.size
        
    def get_hash(self,key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size
    
    def add(self,key,lstValue):
        keyHash = self.get_hash(key)
        keyVal = [key,lstValue]
        
        if self.famStrName[keyHash] is None:
            self.famStrName[keyHash] = list([keyVal])
            return True
        else:
            for item in self.famStrName[keyHash]:
                if item[0] == key:
                    item[1] = lstValue
                    return True
                self.famStrName[keyHash].append(keyVal)
                return True
            
    def get(self,key):
        keyHash = self.get_hash(key)
        if self.famStrName[keyHash] is not None:
            for item in self.famStrName[keyHash]:
                if item[0] == key:
                    return item[1]
    
    def print(self):
        print('List of Family Names')
        for i in self.famStrName:
            if i is not None:
                print(str(i))
                

h = hashList()

h.add('Mom','Eileen')
h.add('Dad','John')
h.add('Son', 'Joseph')
h.add('Daughter', 'Lisa')
h.add('Grandpa','Ralph')
h.add('Grandma','Doris')

h.print()

            