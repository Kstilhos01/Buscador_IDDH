import os
import subprocess

def exibir_menu():
    print("\nMENU:")
    print("1 - Executar Script 1")
    print("2 - Executar Script 2")
    print("3 - Executar Script 3")
    print("0 - Sair")

def executar_script(opcao):
    base_path = os.path.join(os.getcwd(), 'scripts')  # Caminho para a pasta 'scripts'
    
    if opcao == "1":
        script_path = os.path.join(base_path, "script1.py")
        subprocess.run(["python", script_path])
    elif opcao == "2":
        script_path = os.path.join(base_path, "script2.py")
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
