from idf import idf_transform
from tf import tf_transform
from tf_idf import TfIdfTransformer

if __name__ == '__main__':
    count_matrix = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    tf_matrix = tf_transform(count_matrix)
    print(tf_matrix)

    assert tf_matrix == [
        [0.143, 0.143, 0.286, 0.143, 0.143, 0.143, 0, 0, 0, 0, 0, 0],
        [0, 0, 0.143, 0, 0, 0, 0.143, 0.143, 0.143, 0.143, 0.143, 0.143],
    ]

    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    ]
    idf_matrix = idf_transform(count_matrix)
    print(idf_matrix)
    assert idf_matrix == [1.4, 1.4, 1.0, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4]

    tfidf_matrix = [[0.2, 0.2, 0.286, 0.2, 0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                    [0.0, 0.0, 0.143, 0.0, 0.0, 0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]
    transformer = TfIdfTransformer()
    tfidf = transformer.fit_transform(count_matrix)
    assert tfidf == tfidf_matrix
    print(tfidf)
