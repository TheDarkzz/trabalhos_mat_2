from Matriz import Matriz

class Calculos:
    def __init__(self, matriz1, matriz2):
        """Inicializa a classe com duas matrizes para operações."""
        self.matriz1 = matriz1
        self.matriz2 = matriz2

    def soma(self):
        """Soma duas matrizes e retorna o resultado."""
        if self.matriz1.linhas != self.matriz2.linhas or self.matriz1.colunas != self.matriz2.colunas:
            raise ValueError("As matrizes devem ter as mesmas dimensões para serem somadas.")

        matriz_resultante = Matriz(self.matriz1.linhas, self.matriz1.colunas)
        for i in range(self.matriz1.linhas):
            for j in range(self.matriz1.colunas):
                valor_soma = self.matriz1.get_valor(i, j) + self.matriz2.get_valor(i, j)
                matriz_resultante.set_valor(i, j, round(valor_soma, 2))
        
        return matriz_resultante

    def multiplicacao(self):
        """Multiplica duas matrizes e retorna o resultado."""
        if self.matriz1.colunas != self.matriz2.linhas:
            raise ValueError("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz para multiplicação.")

        matriz_resultante = Matriz(self.matriz1.linhas, self.matriz2.colunas)
        for i in range(self.matriz1.linhas):
            for j in range(self.matriz2.colunas):
                valor_multiplicacao = 0
                for k in range(self.matriz1.colunas):
                    valor_multiplicacao += self.matriz1.get_valor(i, k) * self.matriz2.get_valor(k, j)
                matriz_resultante.set_valor(i, j, valor_multiplicacao)
        
        return matriz_resultante
    
    def transpose(self):
        """Retorna a transposta de uma matriz."""
        matriz_transposta = Matriz(self.matriz1.colunas, self.matriz1.linhas)  # A transposta terá dimensões invertidas
        for i in range(self.matriz1.linhas):
            for j in range(self.matriz1.colunas):
                matriz_transposta.set_valor(j, i, self.matriz1.get_valor(i, j))  # Inverte os índices para obter a transposta
        return matriz_transposta
    
    def dot(self):
        dot = int(input("Qual o valor: "))
        matriz_resultante = Matriz(self.matriz1.linhas, self.matriz1.colunas)

        for i in range(self.matriz1.linhas):
            for j in range(self.matriz1.colunas):
                valor_multi = self.matriz1.get_valor(i, j) * dot
                matriz_resultante.set_valor(i, j, valor_multi)
        return matriz_resultante


    def gauss(self):
        matriz_resultante = Matriz(self.matriz1.linhas, self.matriz1.colunas)
        # Copiar os valores da matriz original
        for i in range(self.matriz1.linhas):
            for j in range(self.matriz1.colunas):
                matriz_resultante.set_valor(i, j, self.matriz1.get_valor(i, j))


        # Eliminação Gaussiana
        for i in range(self.matriz1.linhas):
            # Normaliza a linha atual pelo pivô
            pivo = matriz_resultante.get_valor(i, i)
            for j in range(i, self.matriz1.colunas):
                valor = matriz_resultante.get_valor(i, j) / pivo
                matriz_resultante.set_valor(i, j, valor)
            
            # Elimina os elementos abaixo da diagonal
            for k in range(i + 1, self.matriz1.linhas):
                fator = matriz_resultante.get_valor(k, i)
                for j in range(i, self.matriz1.colunas):
                   valor = matriz_resultante.get_valor(k, j) - matriz_resultante.get_valor(i, j) * fator
                   matriz_resultante.set_valor(k, j, round(valor, 2))

            return matriz_resultante

    def solve(self):
            """Resolve o sistema linear Ax = b usando a eliminação de Gauss e retorna o vetor solução."""
            n = self.matriz1.linhas
            matriz_resultante = Matriz(n, self.matriz1.colunas + 1)

            # Matriz aumentada A|b (anexa b à matriz A)
            for i in range(n):
                for j in range(self.matriz1.colunas):
                    matriz_resultante.set_valor(i, j, self.matriz1.get_valor(i, j))
                matriz_resultante.set_valor(i, n, self.matriz2.get_valor(i, 0))  # Coloca b como última coluna

            # Eliminação Gaussiana
            for i in range(n):
                # Normaliza o pivô
                pivo = matriz_resultante.get_valor(i, i)
                for j in range(i, n + 1):  # Inclui a última coluna (termos independentes)
                    valor = matriz_resultante.get_valor(i, j) / pivo
                    matriz_resultante.set_valor(i, j, valor)
                
                # Elimina os elementos abaixo da diagonal
                for k in range(i + 1, n):
                    fator = matriz_resultante.get_valor(k, i)
                    for j in range(i, n + 1):
                        valor = matriz_resultante.get_valor(k, j) - matriz_resultante.get_valor(i, j) * fator
                        matriz_resultante.set_valor(k, j, round(valor, 2))

            # Substituição retroativa
            x = [0 for _ in range(n)]
            for i in range(n - 1, -1, -1):
                x[i] = matriz_resultante.get_valor(i, n)
                for j in range(i + 1, n):
                    x[i] -= matriz_resultante.get_valor(i, j) * x[j]

            return matriz_resultante
