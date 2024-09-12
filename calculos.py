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
                matriz_resultante.set_valor(i, j, valor_soma)
        
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
                   matriz_resultante.set_valor(k, j, valor)

            return matriz_resultante

    def solve(self):
        for i in range(linhas - 1, -1, -1):
            for k in range(i - 1, -1, -1):
                fator = self.matriz1[k][i]
                for j in range(i, colunas):
                    self.matriz1[k][j] -= self.matriz1[i][j] * fator
            
            print(f"Passo {linhas - i} (retroativo) - Matriz após eliminação retroativa da linha {i+1}:")
            print_matrix(self.matriz1)

        # A solução está na última coluna após o escalonamento
        solucao = [self.matriz1[i][-1] for i in range(linhas)]
        return solucao
