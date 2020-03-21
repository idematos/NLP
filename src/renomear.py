def renomear(doc):
    csf = []
    for token in doc:
        if token.pos_ == 'NOUN' or token.pos_ == 'PROPN':
            csf.append('<SUBSTANTIVO>')
        elif token.pos_ == 'VERB' or token.pos_ == 'AUX':
            csf.append('<VERBO>')
        elif token.pos_ == 'ADJ':
            csf.append('<ADJETIVO>')
        elif token.pos_ == 'ADV':
            csf.append('<ADVÉRBIO>')
        elif token.pos_ == 'PUNCT':
            csf.append('<PONTUAÇÃO>')
        elif token.pos_ == 'CCONJ' or token.pos_ == 'SCONJ':
            csf.append('<CONJUNÇÃO>')
        elif token.pos_ == 'PRON':
            csf.append('<PRONOME>')
        elif token.pos_ == 'DET':
            csf.append('<ARTIGO>')
        elif token.pos_ == 'ADP':
            csf.append('<PREPOSIÇÃO>')
        elif token.pos_ == 'NUM':
            csf.append('<NUMERAL>')
        elif token.pos_ == 'SYM':
            csf.append('<SÍMBOLO>')
        elif token.pos_ == 'X':
            csf.append('<PALAVRA ESTRANGEIRA>')
        elif token.pos_ == 'SPACE':
            csf.append('<ESPAÇO>')
    return csf
