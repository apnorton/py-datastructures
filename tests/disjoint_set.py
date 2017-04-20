import unittest
from itertools import combinations
from datastructures.sets import DisjointSet

class TestDisjointSet(unittest.TestCase):

  def test_all_disjoint(self):
    ds = DisjointSet(10)

    for i, j in combinations(range(10), 2):
      self.assertFalse(ds.query(i, j))

  def test_simple_join(self):
    ds = DisjointSet(10)

    ds.join(0, 9)
    self.assertTrue(ds.query(0, 9))
    self.assertFalse(ds.query(4, 9))

    ds.join(0, 4)
    self.assertTrue(ds.query(0, 4))
    self.assertTrue(ds.query(4, 9))

  def test_get_sets(self):
    ds = DisjointSet(10)
    ds.join(0, 1)
    ds.join(0, 2)
    ds.join(0, 3)
    ds.join(5, 6)
    ds.join(6, 7)
    ds.join(4, 8)

    program_result = ds.get_sets()
    human_result = [{0, 1, 2, 3}, {4, 8}, {5, 6, 7}, {9}]
    
    for s in human_result:
      self.assertTrue(s in program_result)
    
    for s in program_result:
      self.assertTrue(s in human_result)

  def test_len(self):
    ds = DisjointSet(10)
    ds.join(0, 1)
    ds.join(0, 2)
    ds.join(0, 3)
    ds.join(5, 4)
    ds.join(5, 7)

    self.assertEqual(len(ds), 5)



if __name__ == '__main__':
  unittest.main()
