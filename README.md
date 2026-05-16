# 📖 Python Project Das MEI

Um projeto Python completo que inclui uma aplicação Streamlit para facilitador de orientação MEI e documentações completas sobre fundamentos e conceitos avançados de Python.

## 🎯 Sobre o Projeto

Este repositório contém:

1. **Aplicação Streamlit** - Facilitador de emissão de guias DAS para MEI
2. **Documentações de Fundamentos e Conceitos de Python**
3. **Estrutura organizada e reutilizável**

## 📁 Estrutura do Repositório

```
PythonProjectDasMei/
│
├── README.md                          # Este arquivo
├── app.py                             # Aplicação principal Streamlit
├── requirements.txt                   # Dependências do projeto
├── packages.txt                       # Pacotes adicionais
│
└── Docs/                              # Documentações
    ├── Fundamentos/
    │   └── Python_Fundamentos.md     # Guia de fundamentos de Python
    │
    ├── Conceitos/
    │   └── Python_Conceitos.md       # Guia de conceitos avançados de Python
    │
└── Teste/                             # Pasta para testes (futura)
    └── Evidencia/                     # Evidências de testes (futura)
```

## 🚀 Aplicação Principal

### Facilitador de Orientação MEI

Uma aplicação Streamlit intuitiva que ajuda usuários leigos a emitir a guia de acordo MEI com segurança.

**Funcionalidades:**
- 🌐 Acesso direto ao sistema oficial da Receita Federal
- 📥 Download de manual em PDF (Roteiro Passo a Passo MEI)
- 🚨 Alertas de segurança e direcionamento
- 💬 Interface amigável e responsiva

### Como Executar a Aplicação

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Executar a aplicação
streamlit run app.py
```

A aplicação abrirá em `http://localhost:8501`

## 📚 Documentações Geradas

### 1. Python - Fundamentos
📄 `Docs/Fundamentos/Python_Fundamentos.md`

**Conteúdo (14 seções):**
- ✅ Introdução ao Python
- ✅ Configuração do Ambiente
- ✅ Estrutura Básica de um Programa
- ✅ Tipos de Dados Fundamentais (int, float, string, bool, None)
- ✅ Operadores (aritméticos, comparação, lógicos)
- ✅ Estruturas de Dados (listas, tuplas, dicionários, sets)
- ✅ Controle de Fluxo (if/elif/else, for, while)
- ✅ Funções (definição, parâmetros, retorno, *args, **kwargs)
- ✅ Tratamento de Erros (try/except/else/finally)
- ✅ Entrada e Saída de Dados
- ✅ Operações com Arquivos (leitura e escrita)
- ✅ Boas Práticas (nomes, docstrings, type checking)
- ✅ Ambiente Virtual (criação e ativação)
- ✅ Resumo de Conceitos-Chave

**Ideal para:** Iniciantes em Python e quem quer revisar os conceitos básicos.

### 2. Python - Conceitos Avançados
📄 `Docs/Conceitos/Python_Conceitos.md`

**Conteúdo (12 seções):**
- ✅ Programação Orientada a Objetos (POO)
  - Classes e Objetos
  - Atributos (instância e classe)
  - Métodos (instância, classe, estáticos)
  - Herança
  - Polimorfismo
  - Encapsulamento
  - Abstração
- ✅ Manipulação de Dados Avançada
  - List/Dictionary/Set Comprehension
  - Generator Expressions
  - Unpacking
- ✅ Funções Avançadas
  - Funções Lambda
  - Map, Filter, Reduce
  - Decoradores
  - Generators
- ✅ Módulos e Pacotes
- ✅ Context Managers
- ✅ Type Hints
- ✅ Exceções Personalizadas
- ✅ Iteradores e Iteráveis
- ✅ Boas Práticas Avançadas (SOLID, Design Patterns)
- ✅ Performance e Otimização (Profiling, Timing)
- ✅ Resumo de Conceitos

**Ideal para:** Desenvolvedores que querem aprimorar seus conhecimentos de Python.

## 💻 Requisitos do Sistema

### Dependências Python
As dependências estão listadas em `requirements.txt`:

```txt
streamlit>=1.30.0
reportlab>=4.0.0
```

### Python Versão
- **Python 3.8+** (recomendado 3.9+)

### Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/gabrielsalesdavid/PythonProjectDasMei.git
cd PythonProjectDasMei
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual:**
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

## 🎓 Como Usar as Documentações

### Para Iniciantes
1. Comece com `Python_Fundamentos.md`
2. Leia cada seção sequencialmente
3. Execute os exemplos de código fornecidos
4. Pratique criando seus próprios programas

### Para Desenvolvedores Intermediários
1. Revise as seções de interesse em `Python_Fundamentos.md`
2. Mergulhe em `Python_Conceitos.md`
3. Explore os padrões de design e boas práticas

### Melhor Forma de Estudar
```python
# Crie arquivos de prática
touch pratica_listas.py
touch pratica_poo.py
touch pratica_decoradores.py

# Execute cada exemplo das documentações
python pratica_listas.py
```

## 📊 Estatísticas do Repositório

| Item | Valor |
|------|-------|
| Linguagem Principal | Python |
| Número de Módulos | 2 (app.py + dependências) |
| Documentações | 2 (Fundamentos + Conceitos) |
| Seções de Documentação | 26 seções totais |
| Exemplos de Código | 100+ exemplos práticos |
| Total de Dependências | 2 pacotes principais |

## 🔗 Links Úteis

### Documentação Oficial
- [Python.org](https://www.python.org)
- [Documentação Python 3](https://docs.python.org/3/)
- [PEP 8 - Style Guide](https://www.python.org/dev/peps/pep-0008/)

### Ferramentas Utilizadas
- [Streamlit](https://streamlit.io) - Framework web Python
- [ReportLab](https://www.reportlab.com) - Geração de PDFs
- [Visual Studio Code](https://code.visualstudio.com) - Editor

### Recursos de Aprendizado
- [Real Python](https://realpython.com/)
- [GeeksforGeeks Python](https://www.geeksforgeeks.org/python-programming-language/)
- [Python Design Patterns](https://refactoring.guru/design-patterns/python)

## 🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**Gabriel Sales David**

- GitHub: [@gabrielsalesdavid](https://github.com/gabrielsalesdavid)
- Repositório: [PythonProjectDasMei](https://github.com/gabrielsalesdavid/PythonProjectDasMei)

## 📅 Histórico de Atualizações

### v1.0.0 - Maio 2026
- ✨ Criação inicial do repositório
- ✨ Aplicação Streamlit para facilitador MEI
- 📚 Documentação de Fundamentos de Python (14 seções)
- 📚 Documentação de Conceitos Avançados de Python (12 seções)
- 📝 README completo com instruções de uso

## 💡 Próximas Melhorias Planejadas

- [ ] Adicionar testes unitários
- [ ] Implementar mais funcionalidades na aplicação Streamlit
- [ ] Criar guias práticos de projetos
- [ ] Adicionar exemplos interativos
- [ ] Documentação sobre frameworks (Django, Flask, FastAPI)
- [ ] Guias de deploy e CI/CD

## ❓ FAQ

**P: Como instalo o projeto?**
R: Clone o repositório, crie um ambiente virtual e execute `pip install -r requirements.txt`. Veja a seção Instalação acima.

**P: Posso usar as documentações em meu projeto?**
R: Sim! As documentações estão disponíveis sob licença MIT.

**P: Como executo a aplicação Streamlit?**
R: Execute `streamlit run app.py` no terminal.

**P: As documentações são adequadas para iniciantes?**
R: Sim! Python_Fundamentos.md é especialmente feita para iniciantes com exemplos práticos.

---

**Última atualização:** Maio 2026

Made with ❤️ by Gabriel Sales David
