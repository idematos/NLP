import spacy as scy
from renomear import renomear

nlp = scy.load('pt')

file = open('reviews_test_estag_nlp.txt','r')

reviews = []
for line in file:
    line = line.replace('\n','')
    reviews.append(line)

classificacao = open('classificacao.txt','w')
filtragem = open('filtragem.txt', 'w')

for review in reviews:
    classificacao.write(review + '\n')
    lreview = review.lower()
    doc = nlp(lreview)
    classes = renomear(doc)
    for i in range(len(classes)):
        classificacao.write(classes[i] + ' ')
        if i >= len(classes) - 2:
            continue
        if classes[i] == '<SUBSTANTIVO>':
            if classes[i+1] == '<ADJETIVO>':
                filtragem.write(doc[i].orth_ + ' ' + doc[i+1].orth_ + '\n')
            if classes[i+1] == '<VERBO>' and classes[i+2] == '<ADJETIVO>':
                filtragem.write(doc[i].orth_ + ' ' + doc[i+1].orth_ + ' ' + doc[i+2].orth_ + '\n')
    if len(classes) > 1:
        if classes[-2] == '<SUBSTANTIVO>' and classes[-1] == '<ADJETIVO>':
            filtragem.write(doc[-2].orth_ + ' ' + doc[-1].orth_ + '\n')
    classificacao.write('\n\n')
classificacao.close()
filtragem.close()
