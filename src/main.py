import spacy as scy

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
    for classe in classes:
        classificacao.write(classe + ' ')
    classificacao.write('\n\n')
    for i in range(len(classes) - 2):
        if classes[i] == '<SUBSTANTIVO>':
            if classes[i+1] == '<ADJETIVO>':
                filtragem.write(doc[i].orth_ + ' ' + doc[i+1].orth_ + '\n')
            if classes[i+1] == '<VERBO>' and classes[i+2] == '<ADJETIVO>':
                filtragem.write(doc[i].orth_ + ' ' + doc[i+1].orth_ + ' ' + doc[i+2].orth_ + '\n')
classificacao.close()
filtragem.close()
