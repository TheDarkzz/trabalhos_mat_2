from Matriz import Matriz
from calculos import Calculos


def main():
    linhas = int(input("Digite o número de linhas: "))
    colunas = int(input("Digite o número de colunas: "))

    # Criando duas instâncias de Matriz
    matriz1 = Matriz(linhas, colunas)
    matriz2 = Matriz(linhas, colunas)

    # Preenchendo as matrizes com valores do usuário2
    print("Preencha a primeira matriz:")
    matriz1.preencher_matriz_com_input()

    print("Preencha a segunda matriz:")
    matriz2.preencher_matriz_com_input()

    # Instanciando a classe Calculos
    calc = Calculos(matriz1, matriz2)

    # Exibindo a matriz
    print("\nPrimeira Matriz preenchida:")
    print(matriz1)
    print("\nSegunda Matriz preenchida:")
    print(matriz2)

    acao = input("Digite a ação (+ para soma, * para multiplicação, D para dot, T para transpose, G para Gaus): ")
    
    if acao == '+':
        result = calc.soma()
        print("Resultado da soma:")
        print(result)
    elif acao == '*':
        result = calc.multiplicacao()
        print("Resultado da multiplicação:")
        print(result)
    elif (acao == 'T'):
        result = calc.transpose()
        print(result)
    elif acao == 'D':
        result = calc.dot()
        print(result)
    elif acao == 'G':
        result = calc.gauss()
        print(result)
    else:
        print("Opção não existente")

if __name__ == "__main__":
    main()
