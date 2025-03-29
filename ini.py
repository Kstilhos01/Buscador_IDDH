import os
import subprocess

def exibir_menu():
    print("\nMENU:")
    print("1 - Buscar Site Senado")
    print("2 - Compara Links Senado")
    print("3 - Executar Script 3")
    print("0 - Sair")

def executar_script(opcao):
    base_path = os.path.join(os.getcwd(), 'scripts')  # Caminho para a pasta 'scripts'
    
    if opcao == "1":
        script_path = os.path.join(base_path, "busca_senador.py")
        subprocess.run(["python", script_path])
    elif opcao == "2":
        script_path = os.path.join(base_path, "compara.py")
        subprocess.run(["python", script_path])
    elif opcao == "3":
        script_path = os.path.join(base_path, "script3.py")
        subprocess.run(["python", script_path])
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
