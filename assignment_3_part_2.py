import random
import time

class HashTableChaining:
    def __init__(self, size=100):
        self.size = 10
        # create input list for each "bucket" in the hash table
        self.table = [[] for _ in range(size)]
    
    def calculate_hash(self, key):
        # we choose to use the built-in python hash function since it is
        # used internally by python built-in data types to calculate hashes
        # and is reliable to prevent collisions
        return hash(key) % self.size
    
    def insert(self, key, value):
        table_idx = self.calculate_hash(key)
        for item in self.table[table_idx]:
            if item[0] == key:
                item[1] = value
                return
        self.table[table_idx].append([key, value])
    
    def search(self, key):
        table_idx = self.calculate_hash(key)
        for item in self.table[table_idx]:
            if item[0] == key:
                return item[1]
        return None
    
    def delete(self, key):
        table_idx = self.calculate_hash(key)
        for x, item in enumerate(self.table[table_idx]):
            if item[0] == key:
                self.table[table_idx].pop(x)
                return True
        return False

# this function will analyze the performance of search, insert, and deletion
# operations for a HashTableChaining across various load factors
def analyze_htc_performance():
    size = 10000
    load_factors = [0.1, 0.25, 1.0, 2.5, 5.0]

    for a in load_factors:
        num_elements = int(a * size)
        htc = HashTableChaining(size=size)

        keys = random.sample(range(10000000), num_elements)
        values = [random.randint(1, 10000) for x in range(num_elements)]

        insert_start = time.time()
        for k, v in zip(keys, values):
            htc.insert(k, v)
        insert_end = time.time()

        search_start = time.time()
        for k in keys:
            htc.search(k)
        search_end = time.time()

        delete_start = time.time()
        for k in keys:
            htc.delete(k)
        delete_end = time.time()

        print(">>>")
        print("Load Factor: " + str(a))
        print("Insert Time: " + str(insert_end - insert_start) + " seconds")
        print("Search Time: " + str(search_end - search_start) + " seconds")
        print("Delete Time: " + str(delete_end - delete_start) + " seconds")
        print("\n")

if __name__ == "__main__":
    analyze_htc_performance()

