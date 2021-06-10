import unittest
from Matriz.matriz import *

class TestMatrix(unittest.TestCase):
    
    def sequenceVerticalTest(self):
        matrix = [
            [1, 3, 2, 4, 5],
            [2, 3, 5, 6, 7],
            [9, 8, 7, 3, 4],
            [4, 8, 6, 7, 3],
            [2, 3, 7, 6, 5],
        ]
        sequence = [5, 7, 6, 7]

        self.assertTupleEqual(matrix.findSequence(matrix, sequence), ((2, 3), (5, 3)))

    def invertedSequenceVerticalTest(self):
        matrix = [
            [1, 3, 2, 4, 5],
            [2, 3, 5, 6, 7],
            [9, 8, 7, 3, 4],
            [4, 8, 6, 7, 3],
            [2, 3, 7, 6, 5]
        ]
        sequence = [8, 8, 3, 3]

        self.assertTupleEqual(matrix.findSequence(matrix, sequence), ((4, 2), (1, 2)))

    def sequenceHorizontalTest(self):
        matrix = [
            [1, 3, 2, 4, 5],
            [2, 3, 5, 6, 7],
            [9, 8, 7, 3, 4],
            [4, 8, 6, 7, 3],
            [2, 3, 7, 6, 5]
        ]
        sequence = [3, 7, 6, 5]

        self.assertTupleEqual(matrix.findSequence(matrix, sequence), ((3, 2), (3, 5)))

    def invertedSequenceHorizontalTest(self):
        matrix = [
            [1, 3, 2, 4, 5],
            [2, 3, 5, 6, 7],
            [9, 8, 7, 3, 4],
            [4, 8, 6, 7, 3],
            [2, 3, 7, 6, 5]
        ]
        sequence = [3, 7, 6, 8]

        self.assertTupleEqual(matrix.findSequence(matrix, sequence), ((4, 5), (4, 2)))

    def coincidenceTest(self):
        matrix = [
            [1, 3, 2, 4, 5],
            [2, 3, 5, 6, 7],
            [9, 8, 7, 3, 4],
            [4, 8, 6, 7, 3],
            [2, 3, 7, 6, 5]
        ]

        self.assertEqual(matrix.findSequence(matrix, sequence), 0)

if __name__ == '__main__':
    unittest.main()
