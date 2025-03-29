def ler_arquivo(nome_arquivo):
    """Lê o arquivo e retorna uma lista de links, removendo quebras de linha e espaços."""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            links = [linha.strip() for linha in arquivo if linha.strip()]
        return set(links)
    except FileNotFoundError:
        print(f"❌ Arquivo '{nome_arquivo}' não encontrado.")
        return set()

def salvar_diferenca(diferenca, nome_arquivo="diferenca_links.txt"):
    """Salva a diferença de links em um arquivo .txt."""
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for link in sorted(diferenca):
            arquivo.write(link + "\n")
    print(f"✅ Arquivo salvo: {nome_arquivo}")

def comparar_arquivos():
    """Compara dois arquivos de links e salva as diferenças."""
    print("📁 Comparação de Links")
    arquivo1 = input("Digite o nome do Arquivo 1 (com extensão .txt): ").strip()
    arquivo2 = input("Digite o nome do Arquivo 2 (com extensão .txt): ").strip()

    # Lê os links dos arquivos
    links_arquivo1 = ler_arquivo(arquivo1)
    links_arquivo2 = ler_arquivo(arquivo2)

    if not links_arquivo1 or not links_arquivo2:
        print("❌ Não foi possível ler um ou ambos os arquivos.")
        return

    # Compara as diferenças
    diferenca = (links_arquivo1 - links_arquivo2) | (links_arquivo2 - links_arquivo1)

    if diferenca:
        salvar_diferenca(diferenca)
    else:
        print("✅ Não há diferenças entre os arquivos!")

if __name__ == "__main__":
    comparar_arquivos()
