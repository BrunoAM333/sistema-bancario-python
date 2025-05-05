# 🏦 Sistema Bancário em Python

Este projeto é uma simulação de um sistema bancário simples, desenvolvido em Python. Inicialmente feito de forma procedural, ele foi refatorado para utilizar **Programação Orientada a Objetos (POO)**, tornando o código mais organizado, reutilizável e de fácil manutenção.

---

## 📌 Funcionalidades

- ✅ Cadastro de usuários com CPF único
- ✅ Criação de contas correntes vinculadas aos usuários
- ✅ Realização de depósitos e saques
- ✅ Geração de extrato bancário
- ✅ Controle de limite de valor por saque e número máximo de saques
- ✅ Listagem de contas cadastradas

---

## 📁 Arquivos do Projeto

| Arquivo                  | Descrição                                 |
|--------------------------|-------------------------------------------|
| `sistema_bancario.py`    | Código principal do sistema bancário (POO) |
| `README.md`              | Documentação do projeto                   |

---

## 🧠 Estrutura Orientada a Objetos

O código é organizado em classes que representam as entidades principais:

- `Cliente`: armazena dados pessoais e contas bancárias do usuário.
- `Conta`: representa a conta bancária com saldo, extrato, limite etc.
- `Banco`: responsável por gerenciar os clientes, contas e operações.

---

## 🚀 Como Executar

1. Instale o Python 3 se ainda não tiver.
2. Clone este repositório:

```bash
git clone https://github.com/BrunoAM333/sistema-bancario-python.git
cd sistema-bancario-python
