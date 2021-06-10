from random import randint

def createList():
    lista = []
    for i in range(10):
        lista.append({"id": i, "edad":randint(1,100)})
        
    return lista

#Use print(createList()) to check

def orderList(lista = createList()):
    listaOrdenada = sorted(
        lista, 
        key = lambda person: person["edad"]
    )
    print(f'Mas joven: {listaOrdenada[0]["id"]}')
    print(f'Mas joven: {listaOrdenada[-1]["id"]}')

    return listaOrdenada

#Use print(orderList()) to check 