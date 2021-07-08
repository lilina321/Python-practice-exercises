
'''
assertEqual - sprawdza czy dwa elementy są równe,
assertNotEqual - sprawdza czy dwa elementy nie są równe,
assertTrue - sprawdza czy wyrażenie/element jest prawdą,
assertFalse - sprawdza czy wyrażenie/element jest fałszem,
assertIn - sprawdza przynależność (czy należy),
assertNotIn - sprawdza przynależność (czy nie należy)


assertListEqual - sprawdza czy dwie listy są równe
assertTupleEqual - sprawdza czy dwie tuple są równe
assertSetEqual - sprawdza czy dwa zbiory są równe
assertDictEqual - sprawdza czy dwa słowniki są równe

'''

import unittest


class SimpleTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(4 + 7, 11)

    def test_sub(self):
        self.assertNotEqual(5 - 3, 3)

    def test_true(self):
        self.assertTrue(3 + 7 == 10)

    def test_false(self):
        self.assertFalse(2 + 6 == 5)

    def test_in(self):
        self.assertIn(2, [1, 2, 3, 4])

    def test_not_in(self):
        self.assertNotIn(15, range(10))

    def test_list(self):
        self.assertListEqual([1, 2, 3], [1, 2, 3])

    def test_tuple(self):
        self.assertTupleEqual((1, 2, 3), (1, 2, 3))

    def test_set(self):
        self.assertSetEqual({1, 2, 3}, {1, 2, 3})

    def test_dict(self):
        self.assertDictEqual({1 : '1', 2: '2'}, {1: '1', 2: '2'})

if __name__ == '__main__':
    unittest.main()
