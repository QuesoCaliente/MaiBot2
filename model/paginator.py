import math
def Paginar(array, pagact, pagtot):
    pagact = pagact - 1
    inic = pagact * pagtot
    finc = (pagact + 1) * pagtot
    return array[inic:finc]


def getPaginas(array, cantItem):
    numero = math.ceil(len(array)/cantItem)
    return numero