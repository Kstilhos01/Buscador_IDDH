  """Busca Proejtos de leis no site do Senado, que contenha a palavra digitada."""
import requests
from bs4 import BeautifulSoup
import time

def buscar_todos_links_senado(url_base):
    """Percorre todas as páginas da busca no Senado e coleta os links dos projetos de lei."""
    links_projetos = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    pagina = 1  # Começa na primeira página

    try:
        while True:
            url_paginada = f"{url_base}&p={pagina}"  # Formato correto da paginação
            print(f"🔎 Buscando na página {pagina}... (Pressione Ctrl + C para encerrar)")

            response = requests.get(url_paginada, headers=headers)
            if response.status_code != 200:
                print(f"❌ Erro ao acessar {url_paginada}: {response.status_code}")
                break

            soup = BeautifulSoup(response.text, 'html.parser')

            # 🟢 Busca todos os links dentro da lista de resultados
            resultados = soup.find_all('a', href=True)

            novos_links = []
            for r in resultados:
                link = r['href']
                if "/materia/" in link:  # Garante que é um link de projeto de lei
                    url_completa = "https://www6g.senado.leg.br" + link if link.startswith("/") else link
                    if url_completa not in links_projetos:
                        novos_links.append(url_completa)

            # 🔴 Se não encontrou novos links, significa que acabou
            if not novos_links:
                print("✅ Fim dos resultados!")
                break

            links_projetos.extend(novos_links)

            pagina += 1  # Avança para a próxima página
            time.sleep(2)  # Aguarda para evitar bloqueios

    except KeyboardInterrupt:
        print("\n🚨 Busca interrompida pelo usuário!")

    return links_projetos

def salvar_txt(links, nome_arquivo):
    """Salva os links dos projetos em um arquivo .txt."""
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for link in links:
            arquivo.write(link + "\n")
    print(f"📂 Arquivo salvo: {nome_arquivo}")

# 🔎 Pergunta ao usuário o termo de busca
termo_busca = input("Digite o termo de busca: ").strip().replace(" ", "+")
url_base = f"https://www6g.senado.leg.br/busca/?colecao=Projetos+e+Matérias+-+Proposições&q={termo_busca}"

# 🔖 Nome do arquivo com o termo de busca
nome_arquivo = f"PL_VD_{termo_busca.replace('+', '_')}.txt"

# Buscar todos os links e salvar os resultados
todos_links = buscar_todos_links_senado(url_base)
salvar_txt(todos_links, nome_arquivo)
