import numpy as np
from itertools import groupby

class DisjointSet:
  def __init__(self, size):
    self.parent   = np.arange(size) # parent of tree rooted at index i
    self.sz       = np.zeros(size) # size of tree rooted at index i
    self.num_sets = size
  
  # Finds the root of given element, c, and returns the root
  # Also flattens the tree as it goes up
  def root(self, c):
    old_c = c
    while c != self.parent[c]:
      self.parent[c] = self.parent[self.parent[c]] # flatten as you go up
      c = self.parent[c]
        
    self.parent[old_c] = c # yep, even more flattening
    return c
  
  # Merges the sets containing c1 and c2
  # Returns True if they were merged, False if they
  # were in the same set
  def join(self, c1, c2):
    r1 = self.root(c1)
    r2 = self.root(c2)

    if r1 == r2:
      return False
    
    # want r1 to be the smaller tree
    # ...allows *some* self-balancing
    if self.sz[r2] < self.sz[r1]:
      (r1, r2) = (r2, r1)
    
    self.parent[r1] = r2
    self.sz[r2]    += self.sz[r2]
    self.num_sets  -= 1
    return True
  
  # Returns true iff c1 and c2 are in the same set
  def query(self, c1, c2):
    return self.root(c1) == self.root(c2)

  # Returns a list of sets described by this collection
  def get_sets(self):
    parent_pairs = [(self.root(x), x) for x in range(len(self.parent))]
    parent_pairs.sort()

    ret_val = [
        set(x[1] for x in pairs) 
        for _, pairs in groupby(parent_pairs, lambda x: x[0])
      ]

    return ret_val
  
  # Returns the number of unique sets in the structure
  def __len__(self):
    return self.num_sets

