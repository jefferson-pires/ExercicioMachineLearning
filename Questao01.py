from sklearn.naive_bayes import MultinomialNB

#[é gordinho?, tem pernas curtas?, ele late?]
porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
marcacoes = ['porco', 'porco', 'porco', 'cachorro', 'cachorro', 'cachorro']
modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

#[é gordinho?, tem pernas curtas?, ele late?]
misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [1, 0, 1]
misterioso4 = [1, 1, 0]
misterioso5 = [0, 0, 0]#erro
misterioso6 = [0, 1, 0]
misterioso7 = [0, 1, 1]
misterioso8 = [0, 0, 1]
#taxa de axerto de 87.5

misteriosos = [misterioso1,misterioso2,misterioso3,misterioso4,misterioso5,misterioso6,misterioso7,misterioso8]

print(modelo.predict(misteriosos))
