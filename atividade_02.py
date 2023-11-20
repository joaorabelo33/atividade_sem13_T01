# Escreva um programa que leia um número n. Considere uma lista com n posições, e então:
# a) preencha com 0 (zero) e imprima a lista;
# b) preencha com os números de 1 a n e imprima a lista;
# c) preencha com valores inteiros lidos pelo teclado e imprima a lista;
# d) preencha na ordem inversa com valores inteiros lidos pelo teclado e imprima a lista; dica: use insert
# para sempre incluir os elementos no início da lista;

def preencher_com_zero(n):
    lista_zero = [0] * n
    print( lista_zero)

def preencher_com_numeros(n):
    lista_numeros = list(range(1, n + 1))
    print(lista_numeros)

def preencher_com_input(n):
    lista_input = [int(input()) for _ in range(n)]
    print(lista_input)

def preencher_inverso_com_input(n):
    lista_inversa = []
    for _ in range(n):
        valor = int(input())
        lista_inversa.insert(0, valor)
    print(lista_inversa)

def main():
    n = int(input())
    
    preencher_com_zero(n)
    preencher_com_numeros(n)
    preencher_com_input(n)
    preencher_inverso_com_input(n)
    
if __name__ == '__main__':
    main()