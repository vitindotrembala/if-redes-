str_uf        = 'Alagoas;Bahia;Ceará;Maranhão;Paraíba;Pernambuco;Piauí;Rio Grande do Norte;Sergipe'
str_siglas    = 'AL;BA;CE;MA;PB;PE;PI;RN;SE'
str_populacao = '3365351;14985284;9240580;7153262;4059905;9674793;3289290;3560903;2338474'

# Preencher as listas a partir das respectivas strings
# lst_uf        <- str_uf
# lst_siglas    <- str_siglas
# lst_populacao <- str_populacao (lembrar de converter para int)

lst_uf = str_uf.split(';')

lst_siglas = str_siglas.split(';')

lst_populacao = str_populacao.split(';')

soma_populacao=0
for pos in range(len(lst_populacao)):
    lst_populacao[pos] = int(lst_populacao[pos])
    soma_populacao = soma_populacao + lst_populacao[pos]
print(lst_uf)
print(lst_siglas)
print(lst_populacao)
print(soma_populacao)