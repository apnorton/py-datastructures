import unittest
from itertools import combinations
from datastructures.trees import DisjointSet

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


if __name__ == '__main__':
  unittest.main()
