import time
from Transformations import Transformations

def get_vector(dimension):
  """Lê um vetor do usuário."""
  components = []
  for i in range(dimension):
    components.append(float(input(f"Digite a componente {i+1}: ")))
  return components

def main():
    transform = Transformations()



    while True:
            print("\n Escolha a transformação:")
            print("1. Translação 2D")
            print("2. Translação 3D")
            print("-------------------------------")
            print("3. Rotação 2D")
            print("4. Rotação em torno de X (3D)")
            print("5. Rotação em torno de Y (3D)")
            print("6. Rotação em torno de Z (3D)")
            print("--------------------------------")
            print("7. Reflexão 2D no eixo X")
            print("8. Reflexão 2D no eixo Y")
            print("9. Reflexão 3D no eixo X")
            print("10. Reflexão 3D no eixo Y")
            print("11. Reflexão 3D no eixo Z")
            print("-------------------------------")
            print("12. Projeção 2D no eixo X")
            print("13. Projeção 2D no eixo Y")
            print("14. Projeção 3D no eixo X")
            print("15. Projeção 3D no eixo Y")
            print("16. Projeção 3D no eixo Z")
            print("------------------------------")
            print("17. Cisalhamento 2DX")
            print("18. Cisalhamento 2DY")
            print("========================")
            print("19. Sair")
            print("")
            print("ASS Melhor Equipe <3")
            print("\033[41m PS Paulo Ricardo o MELHOR PROFESSOR \033[0m")
            print("===========================")

            choice = int(input("Digite o número da transformação: "))

            if choice == 1:  # Translação 2D
                vector = get_vector(2)
                dx = float(input("Digite o deslocamento em x: "))
                dy = float(input("Digite o deslocamento em y: "))
                result = transform.translate2D(vector, dx, dy)
                print(f"Vetor transladado: {result}")

            elif choice == 2:  # Translação 3D
                vector = get_vector(3)
                dx = float(input("Digite o deslocamento em x: "))
                dy = float(input("Digite o deslocamento em y: "))
                dz = float(input("Digite o deslocamento em z: "))
                result = transform.translate3D(vector, dx, dy, dz)
                print(f"Vetor transladado: {result}")

            elif choice == 3:  # Rotação 2D
                vector = get_vector(2)
                angle = float(input("Digite o ângulo de rotação (em graus): "))
                result = transform.rotation2D(vector, angle)
                print(f"Vetor rotacionado: {result}")

            elif choice == 4:  # Rotação em torno de X (3D)
                vector = get_vector(3)
                angle = float(input("Digite o ângulo de rotação (em graus): "))
                result = transform.rotation3DX(vector, angle)
                print(f"Vetor rotacionado: {result}")

            elif choice == 5:  # Rotação em torno de Y (3D)
                vector = get_vector(3)
                angle = float(input("Digite o ângulo de rotação (em graus): "))
                result = transform.rotation3DY(vector, angle)
                print(f"Vetor rotacionado: {result}")

            elif choice == 6:  # Rotação em torno de Z (3D)
                vector = get_vector(3)
                angle = float(input("Digite o ângulo de rotação (em graus): "))
                result = transform.rotation3DZ(vector, angle)
                print(f"Vetor rotacionado: {result}")

            elif choice == 7:  # Reflexão 2D no eixo X
                vector = get_vector(2)
                result = transform.reflection2DX(vector)
                print(f"Vetor refletido no eixo X: {result}")

            elif choice == 8:  # Reflexão 2D no eixo Y
                vector = get_vector(2)
                result = transform.reflection2DY(vector)
                print(f"Vetor refletido no eixo Y: {result}")

            elif choice == 9:  # Reflexão 3D no eixo X
                vector = get_vector(3)
                result = transform.reflection3DX(vector)
                print(f"Vetor refletido no eixo X (3D): {result}")

            elif choice == 10:  # Reflexão 3D no eixo Y
                vector = get_vector(3)
                result = transform.reflection3DY(vector)
                print(f"Vetor refletido no eixo Y (3D): {result}")

            elif choice == 11:  # Reflexão 3D no eixo Z
                vector = get_vector(3)
                result = transform.reflection3DZ(vector)
                print(f"Vetor refletido no eixo Z (3D): {result}")

            elif choice == 12:  # Projeção 2D no eixo X
                vector = get_vector(2)
                result = transform.projection2DX(vector)
                print(f"Projeção no eixo X (2D): {result}")

            elif choice == 13:  # Projeção 2D no eixo Y
                vector = get_vector(2)
                result = transform.projection2DY(vector)
                print(f"Projeção no eixo Y (2D): {result}")

            elif choice == 14:  # Projeção 3D no eixo X
                vector = get_vector(3)
                result = transform.projection3DX(vector)
                print(f"Projeção no eixo X (3D): {result}")

            elif choice == 15:  # Projeção 3D no eixo Y
                vector = get_vector(3)
                result = transform.projection3DY(vector)
                print(f"Projeção no eixo Y (3D): {result}")

            elif choice == 16:  # Projeção 3D no eixo Z
                vector = get_vector(3)
                result = transform.projection3DZ(vector)
                print(f"Projeção no eixo Z (3D): {result}")

            elif choice == 17:  # Cisalhamento 2DX
                vector = get_vector(2)
                kx = float(input("Digite o fator de cisalhamento em x: "))
                result = transform.cisalhamentoX(vector, kx)
                print(f"Vetor cisalhado: {result}")
                
            elif choice == 18:  # Cisalhamento 2DY
                vector = get_vector(2)
                ky = float(input("Digite o fator de cisalhamento em y: "))
                result = transform.cisalhamentoY(vector, ky)
                print(f"Vetor cisalhado: {result}")

            elif choice == 19:  # Sair
                print("Encerrando o programa...")
                break

            else:
                print("Opção inválida. Tente novamente.")
                
            time.sleep(7)
                
if __name__ == "__main__":
    main()
