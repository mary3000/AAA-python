from idf import idf_transform
from tf import tf_transform


class TfIdfTransformer:
    def __init__(self):
        pass

    def fit_transform(self, matrix):
        tf = tf_transform(matrix)
        idf = idf_transform(matrix)

        tf_idf = []
        for text in tf:
            tf_idf.append([round(a * b, 3) for a, b in zip(text, idf)])

        return tf_idf
