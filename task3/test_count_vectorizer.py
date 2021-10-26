import unittest

from count_vectorizer import CountVectorizer


class TestCountVectorizer(unittest.TestCase):

    def assertPermutationEqual(self, first, second):
        return self.assertEqual(sorted(first), sorted(second))

    @staticmethod
    def get_col_reprs(m):
        cols = [''] * len(m[0])
        for i in range(len(m)):
            for j in range(len(m[0])):
                cols[j] += str(m[i][j])
        return cols

    def assertColPermutationEqual(self, first, second):
        fst = self.get_col_reprs(first)
        snd = self.get_col_reprs(second)
        self.assertPermutationEqual(fst, snd)

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
        self.assertColPermutationEqual(m, exp_m)

    def test_interleaving(self):
        cv = CountVectorizer()
        m = cv.fit_transform(['a a a', 'a c a', 'd d a'])
        self.assertPermutationEqual(cv.get_feature_names(), ['a', 'c', 'd'])
        exp_m = [[3, 0, 0],
                 [2, 1, 0],
                 [1, 0, 2]]
        self.assertColPermutationEqual(m, exp_m)

    def test_tab_spaces(self):
        cv = CountVectorizer()
        m = cv.fit_transform(['a a     a', '   a\t\n c a', 'd d a\n\n\n    '])
        self.assertPermutationEqual(cv.get_feature_names(), ['a', 'c', 'd'])
        exp_m = [[3, 0, 0],
                 [2, 1, 0],
                 [1, 0, 2]]
        self.assertColPermutationEqual(m, exp_m)


if __name__ == '__main__':
    unittest.main()
