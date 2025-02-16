# Hash Table 的散列实现

class HashTable:
    def __init__(self) -> None:
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    def hashfunction(self, key):
        return key % self.size

    def rehash(self, oldhash):
        return (oldhash + 1) % self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key)

        # key不存在，散列没有冲突
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            # key出现，替换val
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue)
                # 散列冲突， 再散列，直到找到空的槽或者key
                while self.slots[nextslot] != None and \
                        self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)

            if self.slots[nextslot] == None:
                self.slots[nextslot] = key
                self.data[nextslot] = data
            else:
                self.data[nextslot] = data
    
    def get(self, key):
        startslot = self.hashfunction(key)
        # 标记散列值为查找起点
        data = None
        stop = False
        found = False
        position = startslot
        # 找key直到空槽或者回到起点
        while self.lots[position] != None and \
                not found and not stop:
        # 未找到key，再散列继续查找
            if self.slots[position] == key:
                found = True 
                data = self.data[position]
            else:
                position = self.rehash[position]
                if position == startslot:
                    stop = True
            return data
        
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)    