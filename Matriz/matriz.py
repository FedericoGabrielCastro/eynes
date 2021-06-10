from random import randint

def createMatrix():
    matrix = []

    for n in range(5):
        fila = [randint(0,9) for n in range(5)]
        matrix.append(fila)

    return matrix

def findSequence(matrix, sequence):

    sequence = ''.join(str(n) for n in sequence)

    for row in matrix:
        r = ''.join(str(n) for n in row)
        y = matrix.index(row) + 1
        
        # order sequence
        if sequence[::-1] in r:
            start = 5 -r[::-1].index(str(sequence[0]))
            positionOne = (y, start)
            positionTwo = (y, start - 3)
            return (positionOne, positionTwo)
        elif sequence in r:
            start = r.index(sequence[0] + 1)
            positionOne = (y, start)
            positionTwo = (y, start + 3)
            return (positionOne, positionTwo)

    for column in range(5):
        c = ''.join(str(e[column]) for e in matrix)

        # search Vertical
        if sequence[::1] in c:
            start = 5 - c[::-1].index(str(sequence[0]))
            positionOne = (start, column + 1)
            positionTwo = (int(start) - 3, column + 1)
            return (positionOne, positionTwo)
        elif sequence in c:
            start = c.index(sequence[0]) + 1
            positionOne = (start, column + 1)
            positionTwo = (start + 3, column + 1)
            return (positionOne, positionTwo)

    return 0

        
