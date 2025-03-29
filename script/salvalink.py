import requests
from bs4 import BeautifulSoup

def obter_detalhes_projeto(url):
    """Acessa o link e extrai a ementa, assunto e autoria."""
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"❌ Erro ao acessar {url}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # 📜 Ementa, Assunto e Autoria estão dentro da div específica
    bloco = soup.find('div', class_='span12 sf-bloco-paragrafos-condensados')

    if not bloco:
        print(f"⚠️ Dados não encontrados em {url}")
        return None

    # 🔍 Extração dos dados
    ementa = "Sem ementa"
    assunto = "Sem assunto"
    autoria = "Autor desconhecido"

    for p in bloco.find_all('p'):
        texto = p.text.strip()
        if texto.startswith("Ementa:"):
            ementa = texto.replace("Ementa:", "").strip()
        elif texto.startswith("Assunto:"):
            assunto = texto.replace("Assunto:", "").strip()
        elif texto.startswith("Autoria:"):
            autoria = texto.replace("Autoria:", "").strip()

    return {
        "ementa": ementa,
        "assunto": assunto,
        "autoria": autoria,
        "link": url
    }

def processar_arquivo_links():
    """Solicita o nome do arquivo ao usuário, lê os links e salva os resultados."""
    nome_arquivo_entrada = input("Digite o nome do arquivo com os links (ex: links.txt): ").strip()

    try:
        with open(nome_arquivo_entrada, 'r', encoding='utf-8') as arquivo:
            links = [linha.strip() for linha in arquivo.readlines() if linha.strip()]
    except FileNotFoundError:
        print(f"❌ Arquivo {nome_arquivo_entrada} não encontrado.")
        return
    
    if not links:
        print(f"⚠️ Nenhum link encontrado em {nome_arquivo_entrada}")
        return

    nome_arquivo_saida = "dados_projetos.txt"

    with open(nome_arquivo_saida, 'w', encoding='utf-8') as saida:
        for i, link in enumerate(links, start=1):
            print(f"🔍 Processando {i}/{len(links)}: {link}")
            detalhes = obter_detalhes_projeto(link)
            if detalhes:
                saida.write(f"📜 Ementa: {detalhes['ementa']}\n")
                saida.write(f"📌 Assunto: {detalhes['assunto']}\n")
                saida.write(f"👤 Autoria: {detalhes['autoria']}\n")
                saida.write(f"🔗 Link: {detalhes['link']}\n")
                saida.write("="*50 + "\n")  # Separador entre os projetos
            
    print(f"📂 Arquivo salvo: {nome_arquivo_saida}")

# 📥 Executar o script
processar_arquivo_links()
