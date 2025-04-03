# Buscador_IDDH

1 - Para utilizar baixe o Python 3 - se for windows https://python.org.br/instalacao-windows/

Linux - sudo apt-get install python3.9

Inicar pelo CMD
Abrir o ini.py -  Digite através do CMD - python3 ini.py

![WhatsApp Image 2025-04-02 at 15 19 22](https://github.com/user-attachments/assets/7251eae4-33b9-4b37-95bb-3e713ac0d663)
![WhatsApp Image 2025-04-02 at 15 19 58](https://github.com/user-attachments/assets/2fc25c48-1c36-4799-ae3e-2b735d408c36)
![WhatsApp Image 2025-04-02 at 15 20 26](https://github.com/user-attachments/assets/99bf8fb5-6a2b-4001-beeb-bc0bcf0cc216)

NO PRIMEIRO USO, REALIZAR A INSTALAÇAO DAS DEPENDENCIAS DO SISTEMA.


Buscar Site Senado - Busca links, no site do Senado, onde Projetos de Lei contenha a frase pesquisada, ele busca por frase e palavras da frase.

Compara Links Senado - Se for feita diversas buscas, aqui compara se existem links iguais em dois arquivos de busca, se houver remove e deixa apenas 1 link. Gerando um arquivo novo.

Extrai dados dos Links - Extrai do arquivo final dados como: "ementa"; "assunto"; "autoria"; "link"

Buscar Noticias Google - Para usar este item, deve realizar o cadastro no SerAPI, e gerar uma chave para inserir no script busca_noticia.py
LINK: https://serpapi.com

Dentro da pasta Scritps, abrir o arquivo busca_noticia.py com bloco de notas, e colar a chave no campo.

# Sua API Key do SerpAPI
API_KEY = "colar aqui dentro e salvar o arquivo"
