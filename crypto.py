from cryptography.fernet import Fernet
import os

# Função para gerar uma chave
def gerar_chave():
    """Gera uma nova chave e a salva em um arquivo."""
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)
    print("Chave gerada e salva como 'chave.key'.")

# Função para carregar a chave
def carregar_chave():
    """Carrega a chave do arquivo 'chave.key'."""
    if not os.path.exists("chave.key"):
        raise FileNotFoundError("Arquivo de chave não encontrado. Gere uma chave primeiro.")
    with open("chave.key", "rb") as chave_arquivo:
        return chave_arquivo.read()

# Função para criptografar uma mensagem
def criptografar_mensagem(mensagem):
    """Criptografa uma mensagem usando a chave carregada."""
    chave = carregar_chave()
    fernet = Fernet(chave)
    mensagem_criptografada = fernet.encrypt(mensagem.encode())
    return mensagem_criptografada

# Função para descriptografar uma mensagem
def descriptografar_mensagem(mensagem_criptografada):
    """Descriptografa uma mensagem usando a chave carregada."""
    chave = carregar_chave()
    fernet = Fernet(chave)
    mensagem_descriptografada = fernet.decrypt(mensagem_criptografada).decode()
    return mensagem_descriptografada

# Função principal para executar o programa
def main():
    """Função principal para executar o fluxo de criptografia e descriptografia."""
    # Verifica se a chave já foi gerada
    if not os.path.exists("chave.key"):
        gerar_chave()

    while True:
        print("\nMenu:")
        print("1. Criptografar mensagem")
        print("2. Descriptografar mensagem")
        print("3. Sair")
        opcao = input("Escolha uma opção (1/2/3): ")

        if opcao == '1':
            mensagem = input("Digite a mensagem a ser criptografada: ")
            mensagem_criptografada = criptografar_mensagem(mensagem)
            print("Mensagem criptografada:", mensagem_criptografada)

        elif opcao == '2':
            mensagem_criptografada = input("Digite a mensagem criptografada: ")
            try:
                mensagem_descriptografada = descriptografar_mensagem(mensagem_criptografada.encode())
                print("Mensagem descriptografada:", mensagem_descriptografada)
            except Exception as e:
                print("Erro ao descriptografar:", e)

        elif opcao == '3':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()