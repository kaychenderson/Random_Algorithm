import random

class Page:
    def __init__(self, data: str):
        self.data = data

    def __str__(self):
        return self.data


class GerenciadorMemoria:
    def __init__(self):
        self.ram = [Page("PARTE 3 DE A"), Page("PARTE 1 DE C"), Page("PARTE 2 DE C"), Page("PARTE 3 DE C")]
        self.hd = [
            Page("PARTE 1 DE A"), Page("PARTE 2 DE A"),
            Page("PARTE 1 DE B"), Page("PARTE 2 DE B"),
            Page("PARTE 3 DE B"), Page("PARTE 4 DE B")
        ]

    def realizar_page_in(self):
        index_hd = int(input(f"Qual índice do disco será usado no page in? (0 a {len(self.hd) - 1}): "))
        print(f"Página no índice {index_hd}: {self.hd[index_hd]}")

        index_ram = random.randint(0, len(self.ram) - 1)
        print(f"Página substituída na RAM (índice {index_ram}): {self.ram[index_ram]}")

        self.ram[index_ram] = self.hd[index_hd]
        print(f"Página {self.hd[index_hd]} movida para a RAM.")

    def referenciar_quadro_ram(self):
        index_ram = int(input(f"Qual índice da RAM será referenciado? (0 a {len(self.ram) - 1}): "))
        print(f"Página no índice {index_ram}: {self.ram[index_ram]}")

    def visualizar_ram_hd(self):
        print("\n--- Memória RAM ---")
        self._mostrar_memoria(self.ram)

        print("\n--- Memória HDD ---")
        self._mostrar_memoria(self.hd)

    def _mostrar_memoria(self, memoria):
        print("+----------------------+")
        for i, page in enumerate(memoria):
            print(f"| Índice {i:>2}: {page}")
        print("+----------------------+")

    def menu(self):
        while True:
            print("\n+----------------- MENU ------------------+")
            print("| 1 - REALIZAR PAGE IN                    |")
            print("| 2 - REFERENCIAR QUADRO DA RAM           |")
            print("| 3 - VISUALIZAR RAM E DISCO ATUALMENTE   |")
            print("| 0 - SAIR                                |")
            print("+------------------------------------------+")
            opcao = input("O que deseja fazer? ")

            if opcao == '0':
                print("Encerrando programa...")
                break
            elif opcao == '1':
                self.realizar_page_in()
            elif opcao == '2':
                self.referenciar_quadro_ram()
            elif opcao == '3':
                self.visualizar_ram_hd()
            else:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    gerenciador = GerenciadorMemoria()
    gerenciador.menu()
