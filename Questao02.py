from sklearn.naive_bayes import MultinomialNB

#[possui brilho?, Possui vários metros cúbicos ?, Possui Trasnparência ?, É denso?]
rocha1 = [0,1,0,0]
rocha2 = [1,1,0,0]
rocha3 = [0,1,0,0]
mineral1 = [1,0,1,1]
mineral2 = [0,0,1,1]
mineral3 = [1,0,0,1]

dados = [rocha1, rocha2, rocha3, mineral1, mineral2, mineral3]
marcacoes = ['rocha', 'rocha', 'rocha', 'mineral', 'mineral', 'mineral']
modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

#[possui brilho?, Possui vários metros cúbicos ?, Possui Transparência ?, É denso?]
misterioso1 = [1,0,0,0]
misterioso2 = [1,1,0,0]
misterioso3 = [1,1,1,0]
misterioso4 = [1,1,1,1]
misterioso5 = [0,1,0,0]
misterioso6 = [0,1,1,0]
misterioso7 = [0,1,1,1]
misterioso8 = [0,0,0,0]#erro
misterioso9 = [0,0,1,0]
misterioso10 = [0,0,1,1]
misterioso11 = [0,0,0,1]
misterioso12 = [1,0,1,0]
misterioso13 = [1,0,1,1]
misterioso14 = [1,0,0,1]
misterioso15 = [1,1,0,1]#erro
misterioso16 = [0,1,0,1]

#taxa de erro de 87.5

misteriosos = [misterioso1, misterioso2, misterioso3, misterioso4, misterioso5, misterioso6,misterioso7, misterioso8 ,
               misterioso9, misterioso10, misterioso11, misterioso12, misterioso13, misterioso14, misterioso15,
               misterioso16]

print(modelo.predict(misteriosos))