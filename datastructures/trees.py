import numpy as np

class DisjointSet:
  def __init__(self, size):
    self.parent = np.arange(size) # parent of tree rooted at index i
    self.sz     = np.zeros(size) # size of tree rooted at index i
  
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
  def join(self, c1, c2):
    r1 = self.root(c1)
    r2 = self.root(c2)
    
    # want r1 to be the smaller tree
    # ...allows *some* self-balancing
    if self.sz[r2] < self.sz[r1]:
      (r1, r2) = (r2, r1)
    
    self.parent[r1] = r2
    self.sz[r2]    += self.sz[r2]
  
  # Returns true iff c1 and c2 are in the same set
  def query(self, c1, c2):
    return self.root(c1) == self.root(c2)
