# Python - Fundamentos

## 1. Introdução ao Python

Python é uma linguagem de programação de alto nível, interpretada, com tipagem dinâmica e suporte a múltiplos paradigmas de programação (procedural, orientado a objetos e funcional).

### Características Principais
- **Legibilidade**: Sintaxe clara e simples
- **Interpretada**: Código executado linha por linha
- **Tipagem Dinâmica**: Tipos definidos em tempo de execução
- **Orientada a Objetos**: Suporta classes e heranças
- **Funcional**: Suporta funções como objetos de primeira classe

---

## 2. Configuração do Ambiente

### Instalação do Python
```bash
# Windows
Download em: https://www.python.org

# Linux/Mac
sudo apt-get install python3  # Debian/Ubuntu
brew install python3           # macOS
```

### Verificar Versão
```bash
python --version
python3 --version
```

### Ferramentas Essenciais
- **pip**: Gerenciador de pacotes
- **venv**: Ambiente virtual
- **requirements.txt**: Arquivo de dependências

---

## 3. Estrutura Básica de um Programa

### Primeiro Programa
```python
# Comentário simples
print("Olá, Mundo!")
```

### Comentários
```python
# Comentário de linha única

"""
Comentário de múltiplas linhas
Pode ocupar várias linhas
Também funciona como docstring
"""
```

---

## 4. Tipos de Dados Fundamentais

### Tipos Primitivos

#### Int (Inteiro)
```python
idade = 25
numero = -10
zero = 0
```

#### Float (Ponto Flutuante)
```python
preco = 19.99
temperatura = -5.5
pi = 3.14159
```

#### String (Texto)
```python
nome = "João Silva"
mensagem = 'Olá, Mundo!'
texto_longo = """Este é um
texto de múltiplas linhas"""
```

#### Boolean (Booleano)
```python
ativo = True
desativo = False
```

#### None
```python
valor_nulo = None
```

---

## 5. Operadores

### Operadores Aritméticos
```python
a = 10
b = 3

soma = a + b        # 13
subtracao = a - b   # 7
multiplicacao = a * b  # 30
divisao = a / b     # 3.333...
divisao_inteira = a // b  # 3
modulo = a % b      # 1
potencia = a ** b   # 1000
```

### Operadores de Comparação
```python
resultado = 5 == 5      # True
resultado = 5 != 3      # True
resultado = 5 > 3       # True
resultado = 5 < 3       # False
resultado = 5 >= 5      # True
resultado = 5 <= 3      # False
```

### Operadores Lógicos
```python
resultado = True and False      # False
resultado = True or False       # True
resultado = not True            # False
```

---

## 6. Estruturas de Dados

### Lista
```python
frutas = ["maçã", "banana", "laranja"]
numeros = [1, 2, 3, 4, 5]
mista = [1, "texto", 3.14, True]

# Acessar elementos
primeira = frutas[0]      # "maçã"
ultima = frutas[-1]       # "laranja"

# Adicionar elementos
frutas.append("uva")
frutas.insert(0, "morango")

# Remover elementos
frutas.remove("banana")
elemento = frutas.pop()

# Operações
tamanho = len(frutas)
```

### Tupla
```python
coordenadas = (10, 20)
cores = ("vermelho", "verde", "azul")

# Acessar elementos
x = coordenadas[0]  # 10

# Tuplas são imutáveis - não podem ser modificadas
# tupla.append("novo")  # Erro!
```

### Dicionário
```python
pessoa = {
    "nome": "Maria",
    "idade": 30,
    "cidade": "São Paulo"
}

# Acessar valores
nome = pessoa["nome"]  # "Maria"
nome = pessoa.get("nome")  # Forma segura

# Adicionar/modificar
pessoa["profissao"] = "Engenheira"

# Iterar
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
```

### Conjunto (Set)
```python
numeros = {1, 2, 3, 4, 5}
numeros_duplicados = {1, 1, 2, 2, 3}  # {1, 2, 3}

# Operações de conjunto
numeros.add(6)
numeros.remove(1)
```

---

## 7. Controle de Fluxo

### Condicional if/elif/else
```python
idade = 18

if idade < 13:
    print("Criança")
elif idade < 18:
    print("Adolescente")
else:
    print("Adulto")
```

### Operador Ternário
```python
status = "Maior de idade" if idade >= 18 else "Menor de idade"
```

### Loops - for
```python
# Iterando sobre lista
for fruta in frutas:
    print(fruta)

# Usando range
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):   # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)
```

### Loops - while
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

### Break e Continue
```python
for i in range(10):
    if i == 3:
        continue  # Pula esta iteração
    if i == 7:
        break     # Sai do loop

# Enumerate
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")
```

---

## 8. Funções

### Definição Básica
```python
def saudacao():
    print("Olá!")

saudacao()
```

### Funções com Parâmetros
```python
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("João")
```

### Funções com Valor Padrão
```python
def saudacao(nome="Visitante"):
    print(f"Olá, {nome}!")

saudacao()        # Olá, Visitante!
saudacao("Maria") # Olá, Maria!
```

### Funções com Retorno
```python
def somar(a, b):
    return a + b

resultado = somar(5, 3)  # 8
```

### Múltiplos Retornos
```python
def dividir(a, b):
    quociente = a // b
    resto = a % b
    return quociente, resto

q, r = dividir(10, 3)  # q=3, r=1
```

### *args e **kwargs
```python
def funcao_flexivel(*args, **kwargs):
    print("Argumentos posicionais:", args)
    print("Argumentos nomeados:", kwargs)

funcao_flexivel(1, 2, 3, nome="João", idade=30)
```

---

## 9. Tratamento de Erros

### Try/Except
```python
try:
    numero = int("abc")
except ValueError:
    print("Erro: Digite um número válido!")
except Exception as e:
    print(f"Erro inesperado: {e}")
```

### Else e Finally
```python
try:
    arquivo = open("dados.txt")
except FileNotFoundError:
    print("Arquivo não encontrado")
else:
    print("Arquivo aberto com sucesso")
finally:
    print("Limpando recursos...")
```

---

## 10. Entrada e Saída

### Entrada de Dados
```python
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
```

### Saída de Dados
```python
print("Olá, Mundo!")
print(f"Nome: {nome}, Idade: {idade}")
print("a", "b", "c", sep=", ", end="!\n")
```

### Formatação de Strings
```python
nome = "Maria"
idade = 25

# f-string (Python 3.6+)
print(f"Nome: {nome}, Idade: {idade}")

# format()
print("Nome: {}, Idade: {}".format(nome, idade))

# % (antiga)
print("Nome: %s, Idade: %d" % (nome, idade))
```

---

## 11. Operações com Arquivos

### Leitura
```python
# Ler o arquivo inteiro
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

# Ler linha por linha
with open("dados.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())
```

### Escrita
```python
# Escrever (sobrescreve)
with open("dados.txt", "w") as arquivo:
    arquivo.write("Primeira linha\n")
    arquivo.write("Segunda linha\n")

# Adicionar (append)
with open("dados.txt", "a") as arquivo:
    arquivo.write("Nova linha\n")
```

---

## 12. Boas Práticas

### Convenções de Nomes
```python
# Variáveis e funções: snake_case
meu_nome = "João"
def calcular_total():
    pass

# Classes: PascalCase
class MinhaClasse:
    pass

# Constantes: UPPER_SNAKE_CASE
PI = 3.14159
TAXA_JUROS = 0.05
```

### Docstrings
```python
def somar(a, b):
    """
    Soma dois números.
    
    Args:
        a (int/float): Primeiro número
        b (int/float): Segundo número
    
    Returns:
        int/float: A soma de a e b
    """
    return a + b
```

### Verificar Tipo
```python
valor = "texto"
print(type(valor))  # <class 'str'>

if isinstance(valor, str):
    print("É uma string!")
```

---

## 13. Ambiente Virtual

### Criar Ambiente Virtual
```bash
python -m venv venv
```

### Ativar Ambiente Virtual
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Instalar Dependências
```bash
pip install -r requirements.txt
```

### Desativar Ambiente Virtual
```bash
deactivate
```

---

## 14. Resumo de Conceitos-Chave

| Conceito | Descrição |
|----------|-----------|
| Variável | Contêiner para armazenar dados |
| Tipo de Dado | Classificação do dado (int, str, etc) |
| Operador | Símbolo que realiza operação |
| Condicional | Executa código baseado em condição |
| Loop | Repete código múltiplas vezes |
| Função | Bloco reutilizável de código |
| Estrutura de Dados | Forma de organizar dados |
| Exceção | Erro durante execução |
| Módulo | Arquivo com código reutilizável |
| Pacote | Coleção de módulos |

---

## Próximos Passos
- Estudar Programação Orientada a Objetos (POO)
- Explorar módulos e pacotes
- Aprender sobre comprehensions
- Estudar decoradores e generators
