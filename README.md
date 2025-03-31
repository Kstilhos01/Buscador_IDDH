# Buscador_IDDH
1 - Para utilizar baixe o Python 3 - se for windows https://python.org.br/instalacao-windows/

Linux - sudo apt-get install python3.9

Inicar pelo CMD
Abrir o ini.py - python3 ini.py


Buscar Site Senado - Busca links, no site do Senado, onde Projetos de Lei contenha a frase pesquisada, ele busca por frase e palavras da frase.

Compara Links Senado - Se for feita diversas buscas, aqui compara se existem links iguais em dois arquivos de busca, se houver remove e deixa apenas 1 link. Gerando um arquivo novo.

Extrai dados dos Links - Extrai do arquivo final dados como: "ementa"; "assunto"; "autoria"; "link"

Buscar Noticias Google - Para usar este item, deve realizar o cadastro no SerAPI, e gerar uma chave para inserir no script busca_noticia.py
LINK: https://serpapi.com
