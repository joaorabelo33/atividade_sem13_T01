


def ler_lista(numero):
    lista = []
    soma = 0
    multiplicacao = 1
    
    for i in range(numero):
        numero = int(input())
        
        lista.insert(i, numero)
        soma += numero
        multiplicacao *= numero
    
    return lista , soma, multiplicacao




def main():
    lista, soma, multiplicacao = ler_lista(10)
    
    print(f'{lista}\n{soma}\n{multiplicacao}')
    
    
    
if __name__ == '__main__':
    main()