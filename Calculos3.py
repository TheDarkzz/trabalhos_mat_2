import numpy as np


class Calculos3:
    def __init__(self):
        pass

    def transposta(self, matriz):
        """Calcula a transposta de uma matriz."""
        linhas = len(matriz)
        colunas = len(matriz[0])
        matriz_transposta = [[matriz[j][i] for j in range(linhas)] for i in range(colunas)]
        return matriz_transposta

    def soma(self, matriz1, matriz2):
        """Calcula a soma de duas matrizes."""
        if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
            raise ValueError("As matrizes devem ter as mesmas dimensões para a soma.")
        matriz_soma = [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]
        return matriz_soma

    def multiplicacao(self, matriz1, matriz2):
        """Calcula a multiplicação de duas matrizes ou entre matriz e vetor."""
        # Caso matriz2 seja unidimensional (vetor).
        if isinstance(matriz2[0], (int, float)):
            if len(matriz1[0]) != len(matriz2):
                raise ValueError("O número de colunas da matriz deve ser igual ao tamanho do vetor.")
            resultado = [[sum(matriz1[i][k] * matriz2[k] for k in range(len(matriz2)))] for i in range(len(matriz1))]
            return resultado

        # Caso matriz2 seja bidimensional.
        if len(matriz1[0]) != len(matriz2):
            raise ValueError("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
        linhas = len(matriz1)
        colunas = len(matriz2[0])
        matriz_resultado = [[sum(matriz1[i][k] * matriz2[k][j] for k in range(len(matriz2))) for j in range(colunas)] for i in range(linhas)]
        return matriz_resultado

    def normalizar_vetor(self, vetor):
        """Normaliza um vetor para que seu comprimento seja igual a 1 usando numpy."""
        vetor = np.array(vetor)  # Converte a lista em um array numpy
        norma = np.linalg.norm(vetor)  # Calcula a norma do vetor
        if norma == 0:
            raise ValueError("Não é possível normalizar um vetor de norma zero.")
        vetor_normalizado = vetor / norma  # Divide o vetor pela norma
        return vetor_normalizado.tolist()
    
    #.....
    
   
