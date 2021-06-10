from Simple.simple import createList
import unittest
from Simple.simple import createList

print(createList())

class TestSimple(unittest.TestCase):
    def testCreateList(self):
        lista = createList()
        self.assertEqual(lista, list) #Check list
        self.assertEqual(len(lista), 10) #Check len list

    def testOrderList(self):
        lista = createList()
        listaOrdenada = orderList(lista)
        masJoven = listaOrdenada[0]["edad"]
        masViejo = listaOrdenada[-1]["edad"] 
        self.assertEqual(masViejo>masJoven, true) #Check "masViejo" > "masJoven"
        self.assertGreater(masJoven, masViejo) #Check user "joven" & "viejo"

if __name__ == '__main__':
    unittest.main()