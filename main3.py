from Resolucao import Resolucao
def main():
    matriz = [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0],
    ]

    res = Resolucao(matriz)

    resultado = res.analisar_matriz_adjacencia()
    print("Análise da matriz de adjacência:", resultado)
    print("=======================================")

    autoridade, hub, a0 = res.calcular_hub_autoridade()
    
    print("Autoridade:", autoridade)
    print("Centro:", hub)
    print("a0:", a0)

    print("=======================================")
    autoridade_ordenada = res.ordenar_nos(autoridade)
    hub_ordenado = res.ordenar_nos(hub)
    print("Ordenada por autoridade:", autoridade_ordenada)
    print("Ordenada por centro:", hub_ordenado)
    print("PAULO RICRADO MELHOR PROFESSOR<3")
    
    
 
if __name__ == "__main__":
    main()
