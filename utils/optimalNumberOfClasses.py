import numpy as np


def nombre_de_classes(nbValue):

    if nbValue <= 1:
        return 1
    k = 1 + 3.322 * np.log10(nbValue)
    return round(k)
