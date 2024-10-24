# Criptografia Simples em Python com Fernet

Este projeto implementa um sistema básico de criptografia e descriptografia de mensagens utilizando a biblioteca `cryptography` do Python. O programa permite ao usuário gerar uma chave de criptografia, criptografar mensagens e descriptografá-las de forma segura.

## Funcionalidades

- **Geração de Chave**: Cria uma nova chave de criptografia e a salva em um arquivo chamado `chave.key`.
- **Carregamento de Chave**: Carrega a chave de criptografia a partir do arquivo `chave.key`.
- **Criptografia de Mensagens**: Permite ao usuário criptografar mensagens de texto simples.
- **Descriptografia de Mensagens**: Permite ao usuário descriptografar mensagens criptografadas previamente.
- **Interface Interativa**: Um menu interativo que permite ao usuário escolher entre criptografar, descriptografar ou sair do programa.

## Estrutura do Código

O código é organizado em várias funções:

- `gerar_chave()`: Gera e salva a chave de criptografia.
- `carregar_chave()`: Carrega a chave do arquivo.
- `criptografar_mensagem(mensagem)`: Criptografa uma mensagem utilizando a chave carregada.
- `descriptografar_mensagem(mensagem_criptografada)`: Descriptografa uma mensagem utilizando a chave carregada.
- `main()`: Função principal que gerencia a interação do usuário e o fluxo do programa.

## Dependências

- Python 3.x
- Biblioteca `cryptography`

## Como Usar

1. Clone o repositório:
   ```bash
   git clone <URL do repositório>
   cd <diretório do repositório>
