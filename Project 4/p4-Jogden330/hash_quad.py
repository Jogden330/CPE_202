import math
class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

        #''' Inserts an entry into the hash table (using Horner hash function to determine index,
        # and quadratic probing to resolve collisions).
        # The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        # If the key is not already in the table, the key is inserted along with the associated value
        # If the key is is in the table, the new value replaces the existing value.
        # If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)tyr.'''

    def insert(self, key, value=None):
        index = self.horner_hash(key) % self.table_size

        if self.hash_table[index] != None and self.hash_table[index][0] == key:
              self.hash_table[index] = (key, value)
        else:
            if self.hash_table[index] == None:
                    self.hash_table[index] = (key, value)
                    self.num_items += 1

            else:
                    self.hash_table[self.quadratic_collision(index)] = (key, value)
                    self.num_items += 1


        if (self.get_load_factor() > 0.5):
            self.rehash()

    def quadratic_collision(self, index):
        i = 1
        spot = index
        while(self.hash_table[spot] is not None):
            spot = self.bowns_check(index, i)
            i += 1
        return spot

    def bowns_check(self, index, i):
        spot = index + (i * i)
        while spot >= self.get_table_size():
             spot -= self.get_table_size()

        return spot

    def rehash(self):
        old_table = self.hash_table
        self.hash_table = [None] * self.next_prime(2*self.get_table_size()+1)
        self.table_size = len(self.hash_table)
        self.num_items = 0
        for i in range(len(old_table)):
            if old_table[i] is not None:
                self.insert(old_table[i][0], old_table[i][1])



        # ''' Compute the hash value by using Horner’s rule, as described in project specification.'''
    def horner_hash(self, key):
        hornerkey = 0
        n = min(8, len(key))
        # hornerkey += ord(key[i])
        for i in range(n):
            hornerkey += ord(key[i])*31**(n-1-i)
        return hornerkey

        # ''' Find the next prime number that is > n.'''
    def next_prime(self, N):

        # Base case
        if (N <= 1):
            return 2

        prime = N
        found = False

        # Loop continuously until isPrime returns
        # True for a number greater than n
        while (not found):
            prime = prime + 1

            if (self.isPrime(prime) == True):
                found = True

        return prime

    def isPrime(self, n):
        # Corner cases
        if (n <= 1):
            return False
        if (n <= 3):
            return True

        # This is checked so that we can skip
        # middle five numbers in below loop
        if (n % 2 == 0 or n % 3 == 0):
            return False

        for i in range(5, int(math.sqrt(n) + 1), 6):
            if (n % i == 0 or n % (i + 2) == 0):
                return False

        return True

    # ''' Returns True if key is in an entry of the hash table, False otherwise.'''
    def in_table(self, key):
        i = 0
        index = self.horner_hash(key) % self.table_size
        while (50 > (i / self.get_table_size() * 100)):
            spot = self.bowns_check(index, i)
            if (self.hash_table[spot] is None):
                return False
            elif (self.hash_table[spot][0] == key):
                return True
            i += 1
        return False

    # ''' Returns the index of the hash table entry containing the provided key.
    #         If there is not an entry with the provided key, returns None.'''
    def get_index(self, key):
        i = 0
        index = self.horner_hash(key) % self.table_size
        while (50 > (i / self.get_table_size() * 100)):
            spot = self.bowns_check(index, i)
            if (self.hash_table[spot] is None):
                return None
            elif (self.hash_table[spot][0] == key):
                return spot
            i += 1
        return None


    def get_all_keys(self):
        key_list = [None]* self.get_num_items()
        spot = 0
        for i in range(self.get_table_size()):
            if self.hash_table[i] is not None:
                key_list[spot] = self.hash_table[i][0]
                spot += 1
        return key_list

    # ''' Returns the value associated with the key.
    #     If key is not in hash table, returns None.'''
    def get_value(self, key):
        i = 0
        index = self.horner_hash(key) % self.table_size
        while (50 > (i / self.get_table_size() * 100)):
            spot = self.bowns_check(index, i)
            if (self.hash_table[spot] is None):
                return None
            elif (self.hash_table[spot][0] == key):
                return self.hash_table[spot][1]
            i += 1
        return None


    # ''' Returns the number of entries in the table.'''
    def get_num_items(self):
        return self.num_items

    # ''' Returns the size of the hash table.'''
    def get_table_size(self):
        return self.table_size

    #''' Returns the load factor of the hash table (entries / table_size).'''
    def get_load_factor(self):
        return self.get_num_items()/self.get_table_size()



