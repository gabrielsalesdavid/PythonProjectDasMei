# Python - Conceitos Avançados

## 1. Programação Orientada a Objetos (POO)

### 1.1 Classes e Objetos

Uma classe é um modelo (blueprint) para criar objetos.

```python
class Pessoa:
    """Classe para representar uma pessoa"""
    
    def __init__(self, nome, idade):
        """Construtor - executado ao criar um objeto"""
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        """Método da classe"""
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos"

# Criar objeto (instância)
pessoa1 = Pessoa("João", 30)
print(pessoa1.apresentar())
```

### 1.2 Atributos

**Atributos de Instância**: Únicos para cada objeto
```python
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca       # Atributo de instância
        self.modelo = modelo
    
    def info(self):
        return f"{self.marca} {self.modelo}"

carro = Carro("Toyota", "Corolla")
print(carro.marca)  # Toyota
```

**Atributos de Classe**: Compartilhados por todos os objetos
```python
class Carro:
    total_carros = 0  # Atributo de classe
    
    def __init__(self, marca):
        self.marca = marca
        Carro.total_carros += 1

carro1 = Carro("Toyota")
carro2 = Carro("Ford")
print(Carro.total_carros)  # 2
```

### 1.3 Métodos

**Métodos de Instância**:
```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def saudacao(self):  # Recebe 'self'
        return f"Olá, {self.nome}!"

pessoa = Pessoa("Maria")
print(pessoa.saudacao())
```

**Métodos de Classe** (@classmethod):
```python
class Pessoa:
    total = 0
    
    def __init__(self, nome):
        self.nome = nome
        Pessoa.total += 1
    
    @classmethod
    def total_pessoas(cls):
        return cls.total

print(Pessoa.total_pessoas())
```

**Métodos Estáticos** (@staticmethod):
```python
class Calculadora:
    @staticmethod
    def somar(a, b):
        return a + b

resultado = Calculadora.somar(5, 3)  # 8
```

### 1.4 Herança

Permite que uma classe herde propriedades de outra.

```python
class Animal:
    """Classe pai (superclasse)"""
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        return "Som genérico"

class Cachorro(Animal):
    """Classe filha (subclasse)"""
    def fazer_som(self):
        """Sobrescrita de método"""
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

dog = Cachorro("Rex")
print(dog.fazer_som())  # Au au!

# Usar super() para acessar classe pai
class Cachorro(Animal):
    def fazer_som(self):
        som_pai = super().fazer_som()
        return f"{som_pai} especificamente: Au au!"
```

### 1.5 Polimorfismo

Capacidade de objetos diferentes responderem ao mesmo método.

```python
class Veiculo:
    def acelerar(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        return "Carro acelerando..."

class Bicicleta(Veiculo):
    def acelerar(self):
        return "Bicicleta pedalando..."

# Polimorfismo em ação
veiculos = [Carro(), Bicicleta()]
for veiculo in veiculos:
    print(veiculo.acelerar())
```

### 1.6 Encapsulamento

Proteger atributos através de convenções e propriedades.

```python
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Privado (convenção)
    
    @property
    def saldo(self):
        """Getter"""
        return self.__saldo
    
    @saldo.setter
    def saldo(self, novo_saldo):
        """Setter"""
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            print("Saldo não pode ser negativo")

conta = ContaBancaria(1000)
print(conta.saldo)      # 1000
conta.saldo = 1500      # OK
# print(conta.__saldo)  # Erro! Atributo privado
```

### 1.7 Abstração

```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        """Método abstrato"""
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2

# forma = Forma()  # Erro! Não pode instanciar classe abstrata
quadrado = Quadrado(5)
print(quadrado.calcular_area())  # 25
```

---

## 2. Manipulação de Dados Avançada

### 2.1 List Comprehension

```python
# Forma tradicional
numeros = []
for i in range(10):
    if i % 2 == 0:
        numeros.append(i)

# List comprehension
numeros = [i for i in range(10) if i % 2 == 0]
# [0, 2, 4, 6, 8]

# Mais complexo
quadrados = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]
```

### 2.2 Dictionary Comprehension

```python
# Criar dicionário rapidamente
quadrados = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Com condição
pares = {x: x**2 for x in range(10) if x % 2 == 0}
```

### 2.3 Set Comprehension

```python
unique_nums = {x % 3 for x in range(10)}
# {0, 1, 2}
```

### 2.4 Generator Expressions

```python
# Não cria lista em memória, gera valores sob demanda
geradores = (x**2 for x in range(10))

for valor in geradores:
    print(valor)
```

### 2.5 Unpacking

```python
# Desempacotamento de listas
a, b, c = [1, 2, 3]

# Com *
primeiro, *resto = [1, 2, 3, 4, 5]
# primeiro = 1, resto = [2, 3, 4, 5]

# Desempacotamento de dicionários
def funcao(a, b, c):
    return a + b + c

dados = {"a": 1, "b": 2, "c": 3}
resultado = funcao(**dados)
```

---

## 3. Funções Avançadas

### 3.1 Funções Lambda

Funções anônimas de uma linha.

```python
# Forma tradicional
def quadrado(x):
    return x ** 2

# Lambda
quadrado = lambda x: x ** 2

print(quadrado(5))  # 25

# Uso com map()
numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x ** 2, numeros))
# [1, 4, 9, 16, 25]
```

### 3.2 Map, Filter, Reduce

**map()**: Aplica função a todos elementos
```python
numeros = [1, 2, 3, 4, 5]
dobrados = list(map(lambda x: x * 2, numeros))
# [2, 4, 6, 8, 10]
```

**filter()**: Filtra elementos que atendem critério
```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = list(filter(lambda x: x % 2 == 0, numeros))
# [2, 4, 6, 8]
```

**reduce()**: Reduz lista a um valor único
```python
from functools import reduce

numeros = [1, 2, 3, 4, 5]
produto = reduce(lambda x, y: x * y, numeros)
# 120 (1*2*3*4*5)
```

### 3.3 Decoradores

Funções que modificam o comportamento de outras funções.

```python
def meu_decorador(funcao):
    def wrapper(*args, **kwargs):
        print("Antes da execução")
        resultado = funcao(*args, **kwargs)
        print("Depois da execução")
        return resultado
    return wrapper

@meu_decorador
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("João")
# Output:
# Antes da execução
# Olá, João!
# Depois da execução
```

**Decorador com Parâmetros**:
```python
def repetir(vezes):
    def decorador(funcao):
        def wrapper(*args, **kwargs):
            for _ in range(vezes):
                funcao(*args, **kwargs)
        return wrapper
    return decorador

@repetir(3)
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Maria")
# Imprime "Olá, Maria!" 3 vezes
```

### 3.4 Generators

Funções que retornam múltiplos valores sob demanda.

```python
def contagem(inicio, fim):
    """Generator que produz números"""
    while inicio < fim:
        yield inicio
        inicio += 1

for numero in contagem(1, 5):
    print(numero)
# 1, 2, 3, 4

# Economia de memória
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 1
print(next(gen))  # 2
```

---

## 4. Módulos e Pacotes

### 4.1 Importar Módulos

```python
# Importar módulo inteiro
import math
print(math.pi)      # 3.14159...
print(math.sqrt(16))  # 4.0

# Importar função específica
from math import sqrt, pi
print(sqrt(25))     # 5.0

# Importar com alias
import numpy as np
from datetime import datetime as dt

# Importar tudo (evitar)
from math import *
```

### 4.2 Criar Módulo

**arquivo: uteis.py**
```python
"""Módulo com funções úteis"""

def saudar(nome):
    return f"Olá, {nome}!"

def calcular_idade(ano_nascimento):
    from datetime import datetime
    ano_atual = datetime.now().year
    return ano_atual - ano_nascimento
```

**arquivo: principal.py**
```python
from uteis import saudar, calcular_idade

print(saudar("João"))
print(calcular_idade(1990))
```

### 4.3 Criar Pacote

Estrutura de diretórios:
```
meu_pacote/
    __init__.py
    modulo1.py
    modulo2.py
    sub_pacote/
        __init__.py
        modulo3.py
```

```python
# Importar de pacote
from meu_pacote import modulo1
from meu_pacote.sub_pacote import modulo3
```

---

## 5. Context Managers

Gerenciar recursos (arquivos, conexões, etc).

### 5.1 With Statement

```python
# Abre e fecha automaticamente
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
# Arquivo fechado automaticamente

# Sem with (evitar)
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
arquivo.close()  # Fácil esquecer!
```

### 5.2 Criar Context Manager

```python
from contextlib import contextmanager

@contextmanager
def meu_contexto():
    print("Entrando")
    try:
        yield
    finally:
        print("Saindo")

with meu_contexto():
    print("Dentro do contexto")

# Output:
# Entrando
# Dentro do contexto
# Saindo
```

```python
class MeuContexto:
    def __enter__(self):
        print("Entrando")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saindo")
        return False

with MeuContexto() as ctx:
    print("Dentro do contexto")
```

---

## 6. Type Hints

Indicar tipos esperados (Python 3.5+).

```python
def somar(a: int, b: int) -> int:
    """Soma dois inteiros"""
    return a + b

def processar(nomes: list[str]) -> None:
    for nome in nomes:
        print(nome)

# Com tipos complexos
from typing import List, Dict, Optional, Union

def buscar_usuario(id: int) -> Optional[Dict[str, str]]:
    """Retorna dicionário ou None"""
    pass

def processar_dados(dados: Union[int, str]) -> None:
    """Aceita int ou str"""
    pass
```

---

## 7. Exceções Personalizadas

```python
class IdadeInvalidaError(Exception):
    """Exceção para idade inválida"""
    pass

class SaldoInsuficienteError(Exception):
    """Exceção para saldo insuficiente"""
    pass

def validar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError("Idade não pode ser negativa")
    if idade > 150:
        raise IdadeInvalidaError("Idade muito grande")
    return True

try:
    validar_idade(-5)
except IdadeInvalidaError as e:
    print(f"Erro: {e}")
```

---

## 8. Iteradores e Iteráveis

### 8.1 Protocolo Iterator

```python
class ContadorAte10:
    def __init__(self):
        self.numero = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.numero < 10:
            self.numero += 1
            return self.numero
        else:
            raise StopIteration

for numero in ContadorAte10():
    print(numero)
# 1, 2, 3, ..., 10
```

### 8.2 Iterable vs Iterator

```python
# Iterável: tem __iter__
lista = [1, 2, 3]
iterador = iter(lista)  # Retorna iterator

# Iterator: tem __iter__ e __next__
print(next(iterador))   # 1
print(next(iterador))   # 2
print(next(iterador))   # 3
```

---

## 9. Boas Práticas Avançadas

### 9.1 SOLID Principles

**Single Responsibility**:
```python
# Ruim
class Usuario:
    def __init__(self, nome):
        self.nome = nome
    
    def salvar_bd(self):
        pass  # Responsabilidade do repositório
    
    def enviar_email(self):
        pass  # Responsabilidade do serviço de email

# Bom
class Usuario:
    def __init__(self, nome):
        self.nome = nome

class RepositorioUsuario:
    def salvar(self, usuario):
        pass

class ServicoEmail:
    def enviar(self, usuario):
        pass
```

### 9.2 Design Patterns

**Singleton**:
```python
class Singleton:
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)  # True
```

**Factory**:
```python
class Animal:
    pass

class Cachorro(Animal):
    pass

class Gato(Animal):
    pass

class FabricaAnimal:
    @staticmethod
    def criar_animal(tipo):
        if tipo == "cachorro":
            return Cachorro()
        elif tipo == "gato":
            return Gato()

animal = FabricaAnimal.criar_animal("cachorro")
```

### 9.3 Validação de Dados

```python
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    
    def __post_init__(self):
        if not isinstance(self.nome, str):
            raise ValueError("Nome deve ser string")
        if self.idade < 0:
            raise ValueError("Idade não pode ser negativa")

pessoa = Pessoa("João", 30)  # OK
pessoa = Pessoa("João", -5)  # Erro!
```

---

## 10. Performance e Otimização

### 10.1 Profiling

```python
import cProfile
import pstats

cProfile.run('minha_funcao()')

# Com arquivo
cProfile.run('minha_funcao()', 'perfil')
stats = pstats.Stats('perfil')
stats.sort_stats('cumulative').print_stats(10)
```

### 10.2 Timing

```python
import time

inicio = time.time()
# ... código ...
fim = time.time()
print(f"Tempo: {fim - inicio} segundos")

# Com decorator
import functools

def tempo_execucao(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"{func.__name__} levou {fim - inicio}s")
        return resultado
    return wrapper

@tempo_execucao
def funcao_lenta():
    time.sleep(1)
```

---

## 11. Resumo de Conceitos

| Conceito | Descrição |
|----------|-----------|
| POO | Programação com classes e objetos |
| Herança | Reutilizar código de classe pai |
| Polimorfismo | Mesma interface, comportamentos diferentes |
| Encapsulamento | Proteger dados internos |
| List Comprehension | Criar listas de forma concisa |
| Decorador | Modificar comportamento de função |
| Generator | Produzir valores sob demanda |
| Context Manager | Gerenciar recursos automaticamente |
| Type Hints | Indicar tipos esperados |
| Exception | Tratamento de erros |

---

## 12. Recursos Adicionais

- [Documentação Oficial Python](https://docs.python.org/3/)
- [PEP 8 - Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Real Python](https://realpython.com/)
- [Python Design Patterns](https://refactoring.guru/design-patterns/python)
