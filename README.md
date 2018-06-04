# Demonstração spaCY

## Instruções para executar

É necessário ter o Python instalado (o projeto foi testado usando Python 3.6.5 no macOS).

Primeiro, instale as dependências:

    pip install -r requirements.txt
    
(se preferir, instale as dependências em um _virtual environment_)

Após instalar as dependências é necessário instalar os idiomas:

    python -m spacy download en
    python -m spacy download pt

Para rodar o jupyter notebook:

    jupyter-notebook
    
Com o jupyter rodando, basta selecionar um dos notebooks.

## Usando Docker
    
Para rodar a imagem:

    docker run -p 8888:8888 -v <caminho desse projeto>:/home/jovyan andreroquem/demospacy
    
Ao executar surgirá uma mensagem semelhante a essa:


    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        
Copie e cole a URL em um navegador para acessar os notebooks.            
    
---

Opcionalmente, se quiser construir a imagem localmente:

    docker build . -t <tag>
    
onde <tag> é o nome que você quiser dar para a imagem para usar posteriormente no run.

## Referências

https://spacy.io/usage/
http://mlreference.com/spacy
http://mlreference.com/tokenization-spacy
http://mlreference.com/word-properties-spacy
http://mlreference.com/sentence-boundaries-spacy
http://mlreference.com/token-classes-spacy
http://mlreference.com/dependency-tree-spacy
http://mlreference.com/named-entities-spacy
http://mlreference.com/word-vectors-spacy
https://spacy.io/usage/visualizers
https://spacy.io/usage/linguistic-features    