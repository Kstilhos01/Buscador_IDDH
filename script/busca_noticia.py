import requests
import pandas as pd
import sqlite3

# Sua API Key do SerpAPI
API_KEY = "inserir aqui sua chave do SerAPI"

def buscar_noticias_google(termo_busca, num_resultados, data_inicio, data_fim):
    """Busca notícias no Google News usando a SerpAPI"""
    url = "https://serpapi.com/search"
    params = {
        "q": termo_busca,
        "tbm": "nws",  # Especifica que é uma busca de notícias
        "location": "Brazil",
        "hl": "pt-BR",  # Idioma português do Brasil,
        "gl": "BR",  # Região Brasil,
        "ceid": "BR:pt-419",
        "tbs": f"cdr:1,cd_min:{data_inicio},cd_max:{data_fim}",  # Filtra pelo período especificado
        "num": num_resultados,  # Número de resultados por busca
        "api_key": API_KEY
    }

    response = requests.get(url, params=params)
    dados = response.json()

    noticias = []
    for resultado in dados.get("news_results", []):
        noticia = {
            "Título": resultado.get("title", "N/A"),
            "Data": resultado.get("date", "N/A"),
            "Link": resultado.get("link", "N/A"),
            "Resumo": resultado.get("snippet", "N/A"),
        }
        noticias.append(noticia)

    return noticias

def salvar_noticias_banco(noticias):
    """Salva as notícias no banco de dados SQLite"""
    conn = sqlite3.connect("noticias.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS noticias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        data TEXT,
        link TEXT UNIQUE,
        resumo TEXT
    )""")

    for noticia in noticias:
        try:
            cursor.execute(
                "INSERT INTO noticias (titulo, data, link, resumo) VALUES (?, ?, ?, ?)",
                (noticia["Título"], noticia["Data"], noticia["Link"], noticia["Resumo"])
            )
        except sqlite3.IntegrityError:
            pass  # Evita duplicatas

    conn.commit()
    conn.close()
    print("✅ Notícias salvas no banco de dados!")

def exibir_noticias():
    """Exibe as últimas notícias salvas no banco de dados"""
    conn = sqlite3.connect("noticias.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT titulo, data, link FROM noticias ORDER BY id DESC LIMIT 10")
    noticias = cursor.fetchall()

    if noticias:
        print("\n📜 Últimas notícias salvas:")
        for i, (titulo, data, link) in enumerate(noticias, 1):
            print(f"{i}. {titulo} ({data}) - 🔗 {link}")
    else:
        print("⚠ Nenhuma notícia encontrada no banco de dados.")

    conn.close()

def exportar_banco_dados():
    """Exporta os dados do banco para CSV/Excel"""
    conn = sqlite3.connect("noticias.db")
    df = pd.read_sql_query("SELECT * FROM noticias", conn)
    conn.close()

    df.to_csv("noticias_banco.csv", index=False, encoding="utf-8")
    df.to_excel("noticias_banco.xlsx", index=False)

    print("📂 Banco de dados exportado para 'noticias_banco.csv' e 'noticias_banco.xlsx'!")

def menu():
    """Menu interativo para busca de notícias"""
    while True:
        print("\n📢 MENU - Sistema de Busca de Notícias 📢")
        print("1️⃣ Buscar notícias por palavras-chave")
        print("2️⃣ Exibir últimas notícias salvas")
        print("3️⃣ Exportar banco de dados para CSV/Excel")
        print("0️⃣ Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            termos = input("Digite os termos de busca separados por vírgula: ").split(",")
            num_resultados = int(input("Digite o número de resultados desejados (exemplo: 20): "))
            
            print("\nDigite o período desejado:")
            data_inicio = input("Data de início (exemplo: 01/01/2024): ")
            data_fim = input("Data de fim (exemplo: 06/30/2024): ")

            todas_noticias = []
            for termo in termos:
                print(f"🔎 Buscando notícias para: {termo.strip()}...")
                noticias = buscar_noticias_google(termo.strip(), num_resultados, data_inicio, data_fim)
                todas_noticias.extend(noticias)

            salvar_noticias_banco(todas_noticias)

        elif opcao == "2":
            exibir_noticias()

        elif opcao == "3":
            exportar_banco_dados()

        elif opcao == "0":
            print("👋 Saindo do sistema...")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

# 🔹 Inicia o menu interativo
menu()
