import os
import subprocess
import sys


def exibir_menu():
    print("\nMENU:")
    print("1 - Buscar Site Senado")
    print("2 - Compara Links Senado")
    print("3 - Extrai dados dos Links")
    print("4 - Busca Notícias Google")
    print("5 - Instalar Dependências do Sistema")
    print("0 - Sair")


def atualizar_pip():
    try:
        print("\nVerificando atualização do pip...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
            check=True
        )
        print("pip atualizado com sucesso.\n")
    except subprocess.CalledProcessError:
        print("Falha ao atualizar o pip. Continuando com a versão atual.\n")


def instalar_dependencias():
    atualizar_pip()

    # Apenas bibliotecas externas (pip)
    dependencias = [
        "requests",
        "pandas",
        "beautifulsoup4"
    ]

    for dependencia in dependencias:
        try:
            print(f"Instalando dependência: {dependencia}")
            subprocess.run(
                [sys.executable, "-m", "pip", "install", dependencia],
                check=True
            )
            print(f"Dependência '{dependencia}' instalada com sucesso.\n")
        except subprocess.CalledProcessError:
            print(f"Erro ao instalar a dependência '{dependencia}'. Verifique manualmente.\n")


def executar_script(opcao):
    base_path = os.path.join(os.getcwd(), 'script')

    if opcao == "1":
        subprocess.run([sys.executable, os.path.join(base_path, "buscador_senado.py")])
    elif opcao == "2":
        subprocess.run([sys.executable, os.path.join(base_path, "compara.py")])
    elif opcao == "3":
        subprocess.run([sys.executable, os.path.join(base_path, "salvalink.py")])
    elif opcao == "4":
        subprocess.run([sys.executable, os.path.join(base_path, "busca_noticia.py")])
    elif opcao == "5":
        instalar_dependencias()
    elif opcao == "0":
        print("Saindo...")
        sys.exit()
    else:
        print("Opção inválida. Tente novamente.")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        executar_script(opcao)


if __name__ == "__main__":
    main()
