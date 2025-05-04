#input em python
# input() é uma função que lê a entrada de dados do usuário, e retorna essa entrada como uma string.

# A função input() exibe a mensagem "Qual é o seu nome? " e aguarda o usuário digitar algo.
# Após o usuário pressionar Enter, o valor digitado é armazenado na variável nome.
# Em seguida, a função print() exibe a mensagem "Olá, {nome}! Seja bem-vindo(a) ao curso de Python!", onde {nome} é substituído pelo valor armazenado na variável nome.

#exemplo:

#opcao 0
nome = input("Qual é o seu nome? ")
print("Olá, " + nome + "! Seja bem-vindo(a) ao curso de Python!")
#o operador + é usado para concatenar strings.

#opção 1
nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}! Seja bem-vindo(a) ao curso de Python!")
# A sintaxe f"Olá, {nome}!" é uma f-string (string formatada) que permite incluir expressões dentro de chaves {}.

#opção 2
nome = input("Qual é o seu nome? ")
print("Olá, {}! Seja bem-vindo(a) ao curso de Python!".format(nome))
# A função format() é usada para formatar strings. O método format() substitui os campos de marcador de posição em uma string com os valores fornecidos.

#opção 3
nome = input("Qual é o seu nome? ")
print("Olá, %s! Seja bem-vindo(a) ao curso de Python!" % nome)
# A sintaxe %s é um operador de formatação de string que substitui o marcador %s pelo valor da variável nome. 
# Essa forma de formatação é mais antiga e menos recomendada em comparação com as opções anteriores, mas ainda é válida.

#opção 4
nome = input("Qual é o seu nome? ")
print("Olá, {0}! Seja bem-vindo(a) ao curso de Python!".format(nome))
# A sintaxe {0} é um marcador de posição que será substituído pelo valor da variável nome. 
#Essa forma de formatação é semelhante à opção 2, mas usa índices para especificar a posição do valor a ser inserido.
