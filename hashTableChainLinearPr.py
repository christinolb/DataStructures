class HashTable:  
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]
        
    def get_hash(self, key):
        try:
            hash = 0
            for char in key:
                hash += ord(char)
            return hash % self.max
        except TypeError:
            return key % self.max

    def rehash(self,oldhash):
        return (oldhash+1) % self.max
    
    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]

    def full(self):
        f = False
        for i in self.arr:
            if i != None:
                f = True
            else:
                f = False
        return f
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] == None:
            self.arr[h].append((key,val))
        #linear probing
        nextslot = self.rehash(h)
        while self.arr[nextslot] != None:
            nextslot = self.rehash(nextslot)
            if self.arr[nextslot] == None:
                self.arr[nextslot].append((key,val))
            if self.full() == True:
                break
                
            
        #chaining
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))
        
    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del",index)
                del self.arr[arr_index][index]



def main():
    t = HashTable()
    
    t["Bryce Harper"] = 0.336735
    t["Christian Yelich"] = 0.311321
    t["Francisco Cervelli"] = 0.315068
    t["Gleyber Torres"] = 0.242105
    t["Jean Segura"] = 0.315217
    t["Mike Zunino"] = 	0.186667
    t["Mookie Betts"] = 0.347368
    t["Trevor Story"] = 0.291262
    
    
    
    

    print(t.arr)
    
main()
