import os
import subprocess

def exibir_menu():
    print("\nMENU:")
    print("1 - Buscar Site Senado")
    print("2 - Compara Links Senado")
    print("3 - Extrai dados dos Links")
    print("4 - Busca Notícias Google")
    print("5 - Instalar Dependências do Sistema")
    print("0 - Sair")

def instalar_dependencias():
    # Lista das bibliotecas a serem instaladas
    dependencias = ["os", "subprocess", "requests", "pandas", "sqlite3" , "bs4"]
    
    for dependencia in dependencias:
        try:
            # Executa o comando pip para instalar a biblioteca
            subprocess.run(["pip", "install", dependencia], check=True)
            print(f"Dependência '{dependencia}' instalada com sucesso.")
        except subprocess.CalledProcessError:
            print(f"Erro ao instalar a dependência '{dependencia}'. Verifique manualmente.")

def executar_script(opcao):
    base_path = os.path.join(os.getcwd(), 'script')  # Caminho para a pasta 'scripts'
    
    if opcao == "1":
        script_path = os.path.join(base_path, "buscador_senado.py")
        subprocess.run(["python", script_path])
    elif opcao == "2":
        script_path = os.path.join(base_path, "compara.py")
        subprocess.run(["python", script_path])
    elif opcao == "3":
        script_path = os.path.join(base_path, "salvalink.py")
        subprocess.run(["python", script_path])
    elif opcao == "4":
        script_path = os.path.join(base_path, "busca_noticia.py")
        subprocess.run(["python", script_path])
    elif opcao == "5":
        instalar_dependencias()
    elif opcao == "0":
        print("Saindo...")
        exit()
    else:
        print("Opção inválida. Tente novamente.")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        executar_script(opcao)

if __name__ == "__main__":
    main()
