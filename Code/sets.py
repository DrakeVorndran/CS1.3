from hashtable import HashTable

class Set(object):
  def __init__(self, values=[]):
    self.size = 0
    self.table = HashTable()
    for i in values:
      if not self.contains(i):
        self.add(i)

  def __repr__(self):
    return "Set: " + str(self.table.keys())

  def __str__(self):
    return str(self.table.keys())

  def __iter__(self):
    return self

  def __next__(self):
    pass
  
  def contains(self, item): # avg: O(1) worst: O(l) where l is the load factor of the table
    return self.table.contains(item) # avg: O(1) worst: O(l) where l is the load factor of the table
  
  def add(self, item): #O(1)
    if self.contains(item): #O(1)
      raise ValueError("Set already contains item: {}".format(item))
    self.size += 1
    self.table.set(item, None) #O(1)
  
  def remove(self, item): #O(1)
    if not self.contains(item): #O(1)
      raise ValueError("Set does not contain item: {}".format(item))
    self.size -= 1
    self.table.delete(item) #O(1)

  def items(self):
    return self.table.keys()

  def union(self, set2): #O(nm)
    s1_vals = self.items() # O(n)
    s2_vals = set2.items() # O(m)
    return_set = Set() 
    for i in s1_vals: # O(n)
      if not return_set.contains(i): #O(1)
        return_set.add(i)
    for i in s2_vals: # O(m)
      if not return_set.contains(i): #O(1)
        return_set.add(i)
    return return_set

  def intersection(self, set2): # O(m)
    return_set = Set()
    s2_vals = set2.items() # O(m)
    for i in s2_vals: # O(m)
      if self.contains(i) and not return_set.contains(i): # O(1)
        return_set.add(i) # O(1)
    return return_set

  def difference(self, set2): # O(m)
    return_set = Set()
    s1_vals = self.items() # O(m)
    for i in s1_vals: # O(m)
      if not set2.contains(i) and not return_set.contains(i): # O(1)
        return_set.add(i) # O(1)
    return return_set

  def is_subset(self, set2): # O(m)
    s2_vals = set2.items() # O(m)
    for i in s2_vals: # O(m)
      if not self.contains(i): # O(1)
        return False
    return True
    

def main():
  s = Set()
  print(s)
  s.add(1)
  print(s)
  s.add(2)
  print(s)
  s.add(3)
  print(s)
  s.remove(2)
  print(s)
  s.remove(1)
  print(s)
  s.remove(3)
  print(s)

if __name__ == "__main__":
  main()  
    
      


