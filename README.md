<h1 align="center" style="font-weight: bold;">🖥️ Gerenciador de Memória Paginada: Algoritmo Aleatório 💾</h1> 
<p align="center"> 
    <a href="#about">Sobre o Projeto</a> • 
    <a href="#features">Funcionalidades</a> • 
    <a href="#install">Instalação</a> • 
    <a href="#usage">Como Usar</a> •
    <a href="#code">Descrição do Código</a> •
    <a href="#output">Saída do Código</a>
</p>

### 📌 Disciplina: PEX0093 Sistemas Operacionais
##### Professor:  [Raí Emanuel](https://github.com/rai-e)
##### Discentes: Amanda Gonçalves, Amanda Santiago, Joana Larissa e Kayc Henderson

#### 🎓 Bacharelado Interdisciplinar em Tecnologia da Informação <br> 🏫 Universidade Federal Rural do Semi-Árido - (UFERSA)

---

<h2 id="tech" style="font-weight: bold; font-size: 2rem">🛠️ Tecnologia Utilizada</h2> 
<img align="center" alt="python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>

---

<h2 id="about" style="font-weight: bold; font-size: 2rem">📖 Sobre o Projeto</h2>
Este projeto implementa um **Gerenciador de Memória Paginada** simulado em Python. Ele representa a memória RAM e o HD, permitindo operações como:

- **Page In:** Transferência de páginas do HD para a RAM, substituindo uma página existente.
- **Referência a Quadros:** Acesso e visualização de páginas na RAM.
- **Visualização da Memória:** Exibição do estado atual da RAM e do HD.

A implementação demonstra conceitos fundamentais de **gestão de memória em sistemas operacionais**, incluindo paginação, substituição de páginas e hierarquia de armazenamento.

---

<h2 id="features" style="font-weight: bold; font-size: 2rem">⚙️ Funcionalidades</h2> 

✅ **Simulação de memória RAM e HD**  
✅ **Algoritmo de substituição aleatória para Page In**  
✅ **Acesso e visualização de páginas na memória**  
✅ **Interface interativa via terminal**  

---

<h2 id="install" style="font-weight: bold; font-size: 2rem">📦 Instalação</h2>
Para executar o código em sua máquina, siga os passos abaixo:

#### 1️⃣ Clone este repositório:
```bash
git clone https://github.com/kaychenderson/Random_Algorithm.git  
```

#### 2️⃣ Acesse o diretório do projeto:
```bash
cd Random_Algorithm
```

#### 3️⃣ Execute o programa:
```bash
python random_alg.py
```

<h2 id="usage" style="font-weight: bold; font-size: 2rem">💡 Como Usar</h2> 
Após iniciar o programa, um **menu interativo** será exibido no terminal:

```bash
+----------------- MENU ------------------+
| 1 - REALIZAR PAGE IN                    |
| 2 - REFERENCIAR QUADRO DA RAM           |
| 3 - VISUALIZAR RAM E DISCO ATUALMENTE   |
| 0 - SAIR                                |
+------------------------------------------+
O que deseja fazer?
```


#### 📌 Explicação das opções:
🔹 Opção 1 - Realizar Page In:
➡️ Escolha uma página do HD para ser carregada na RAM, substituindo uma existente.

🔹 Opção 2 - Referenciar Quadro da RAM: 
➡️ Exibe o conteúdo de uma página na RAM. (Opção somente utilizada para outros algoritmos)

🔹 Opção 3 - Visualizar RAM e HD:
➡️ Mostra o estado atual das memórias.

🔹 Opção 0 - Sair:
➡️ Encerra o programa.

<h2 id="code" style="font-weight: bold; font-size: 2rem">📝 Descrição do Código</h2>
O código é estruturado da seguinte forma:

#### 📌 1. Classe Page
```bash
class Page:
    def __init__(self, data: str):
        self.data = data

    def __str__(self):
        return self.data
```
- Representa uma página de memória, armazenando um pedaço de informação.
- O método __str__ permite exibir o conteúdo da página.

#### 📌 2. Classe GerenciadorMemoria
```bash
class GerenciadorMemoria:
    def __init__(self):
        self.ram = [Page("PARTE 3 DE A"), Page("PARTE 1 DE C"), Page("PARTE 2 DE C"), Page("PARTE 3 DE C")]
        self.hd = [
            Page("PARTE 1 DE A"), Page("PARTE 2 DE A"),
            Page("PARTE 1 DE B"), Page("PARTE 2 DE B"),
            Page("PARTE 3 DE B"), Page("PARTE 4 DE B")
        ]
```
- Atributo ram: Lista representando a memória RAM com páginas iniciais.
- Atributo hd: Lista representando o HD com páginas armazenadas.

#### 📌 3. Método realizar_page_in()
```bash
def realizar_page_in(self):
    index_hd = int(input(f"Qual índice do disco será usado no page in? (0 a {len(self.hd) - 1}): "))
    index_ram = random.randint(0, len(self.ram) - 1)

    self.ram[index_ram] = self.hd[index_hd]
    print(f"Página {self.hd[index_hd]} movida para a RAM.")
```
- Solicita um índice de página no HD.
- Escolhe aleatoriamente um quadro da RAM para substituição.
- Substitui a página e exibe o resultado.

#### 📌 4. Método visualizar_ram_hd()
```bash
def visualizar_ram_hd(self):
    print("\n--- Memória RAM ---")
    self._mostrar_memoria(self.ram)
    print("\n--- Memória HDD ---")
    self._mostrar_memoria(self.hd)
```
- Exibe o conteúdo atual da RAM e do HD.

<h2 id="output" style="font-weight: bold; font-size: 2rem">📊 Exemplo de Saída do Código</h2>

#### 📌 Exemplo de operação de "Page In":
```bash
+----------------- MENU ------------------+
| 1 - REALIZAR PAGE IN                    |
| 2 - REFERENCIAR QUADRO DA RAM           |
| 3 - VISUALIZAR RAM E DISCO ATUALMENTE   |
| 0 - SAIR                                |
+------------------------------------------+
O que deseja fazer? 1

Qual índice do disco será usado no page in? (0 a 5): 2
Página no índice 2: PARTE 1 DE B
Página substituída na RAM (índice 1): PARTE 1 DE C
Página PARTE 1 DE B movida para a RAM.
```
#### 📌 Exemplo de visualização da RAM e HD:
```bash
--- Memória RAM ---
+----------------------+
| Índice  0: PARTE 3 DE A |
| Índice  1: PARTE 1 DE B |
| Índice  2: PARTE 2 DE C |
| Índice  3: PARTE 3 DE C |
+----------------------+

--- Memória HDD ---
+----------------------+
| Índice  0: PARTE 1 DE A |
| Índice  1: PARTE 2 DE A |
| Índice  2: PARTE 1 DE B |
| Índice  3: PARTE 2 DE B |
| Índice  4: PARTE 3 DE B |
| Índice  5: PARTE 4 DE B |
+----------------------+
```
