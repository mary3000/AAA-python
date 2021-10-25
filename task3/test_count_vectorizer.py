import unittest
from count_vectorizer import CountVectorizer


class TestCountVectorizer(unittest.TestCase):

    def assertPermutationEqual(self, first, second):
        return self.assertEqual(sorted(first), sorted(second))

    def test_missing_fit_transform(self):
        cv = CountVectorizer()
        self.assertEqual(cv.get_feature_names(), [])

    def test_empty(self):
        cv = CountVectorizer()
        cv.fit_transform([])
        self.assertEqual(cv.get_feature_names(), [])

    def test_empty_texts(self):
        cv = CountVectorizer()
        cv.fit_transform(['', '', ''])
        self.assertEqual(cv.get_feature_names(), [])

    def test_all_distinct(self):
        cv = CountVectorizer()
        m = cv.fit_transform(['a b c', 'd e f', 'g h i'])
        self.assertPermutationEqual(cv.get_feature_names(), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
        exp_m = [[1, 1, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 1, 1]]



if __name__ == '__main__':
    unittest.main()
