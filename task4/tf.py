def tf_transform(matrix):
    tf = []
    for text in matrix:
        row = []
        for occ in text:
            row.append(round(occ / sum(text), 3))
        tf.append(row)
    return tf
