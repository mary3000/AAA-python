class CountVectorizer():
    def __init__(self):
        self._feature_names = []

    def fit_transform(self, corpus):
        self._init_features(corpus)
        return self._get_matrix(corpus)

    def get_feature_names(self):
        return self._feature_names

    def _init_features(self, corpus):
        feature_names = {word.lower() for text in corpus for word in text.split()}
        self._feature_names = list(feature_names)

    def _get_matrix(self, corpus):
        matrix = []
        for text in corpus:
            matrix.append([])
            for word in self._feature_names:
                text_words = [word.lower() for word in text.split()]
                matrix[-1].append(text_words.count(word))

        return matrix
