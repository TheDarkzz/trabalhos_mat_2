import numpy as np
from Calculos import Calculos3


class Resolucao:
    
    
    def __init__(self, matriz):
        """
        Inicializa a classe com uma matriz de adjacência para operações.
        """
        self.matriz = matriz
        self.calculo = Calculos3()
        
    
    def analisar_matriz_adjacencia(self):
        """
        Analisa a matriz de adjacência e retorna informações sobre o grafo.
        """
        n = len(self.matriz)
        graus = [sum(self.matriz[i]) for i in range(n)]
        conexoes = [(i, j) for i in range(n) for j in range(n) if self.matriz[i][j] != 0]

        matriz_transposta = self.calculo.transposta(self.matriz)
        n = len(matriz_transposta)
        autoridade = [sum(matriz_transposta[i]) for i in range(n)]


        return {
            "vetor centro inicial": graus,
            "vetor autoridade inicial": autoridade
        }

    def calcular_hub_autoridade(self, iteracoes=100, tol=1e-6):
        n = len(self.matriz)
        hub = [sum(self.matriz[i]) for i in range(n)]
        conexoes = [(i, j) for i in range(n) for j in range(n) if self.matriz[i][j] != 0]

        matriz_transposta = self.calculo.transposta(self.matriz)
        n = len(matriz_transposta)
        autoridade = [sum(matriz_transposta[i]) for i in range(n)]

        matriz_1 = self.matriz
        colunas = [[linha[i] for linha in self.matriz] for i in range(len(self.matriz[0]))]
        print("Colunas: ",colunas)

        for i in range(len(autoridade)):
            a0 = self.calculo.multiplicacao(colunas, autoridade)

        for _ in range(iteracoes):


            nova_autoridade = self.calculo.multiplicacao(matriz_transposta, hub)
            # Calcula o novo vetor de hub
            nova_hub = self.calculo.multiplicacao(self.matriz, autoridade)

            # Normaliza os vetores
            nova_autoridade = self.calculo.normalizar_vetor(nova_autoridade)
            nova_hub = self.calculo.normalizar_vetor(nova_hub)

            # Verifica convergência
            
            autoridade, hub = nova_autoridade, nova_hub

        return autoridade, hub, a0
    
    def calcular_norma(self):

        matriz = np.array(self)

        return np.sqrt(np.sum(self**2))


    def ordenar_nos(self, vetor):
        """
        Ordena os nós com base nos valores de um vetor (ex: hub ou autoridade).
        Retorna uma lista de tuplas no formato (índice, valor), ordenada em ordem decrescente.
        """
        return sorted(
        [(i, float(v[0]) if isinstance(v, list) else float(v)) for i, v in enumerate(vetor)], 
        key=lambda x: x[1], 
        reverse=True
    )
