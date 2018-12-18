# NLP
Essa é uma aplicação Python 3.6 que classifica gramaticalmente, identifica e retira padrões pré-definidos de palavras e símbolos em um arquivo .txt contendo frases em linguagem natural (pt-br).

**Instalação de requisitos:** 

    $ pip3 install spacy

    $ python3 -m spacy download pt

**Uso**: 

    $ python3 main.py

## Saída

**classificacao.txt:** todas as frases do arquivo de entrada seguidas de sua classificação gramatical por palavra.

**filtragem.txt:** trechos das frases do arquivo de entrada que seguem um dos padrões: 

                        <SUBSTANTIVO> + <ADJETIVO> ou <SUBSTANTIVO> + <VERBO> + <ADJETIVO>
