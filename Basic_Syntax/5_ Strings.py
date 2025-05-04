couser = "Curso de Python" #objeto str
couser.upper()# método upper() retorna o valor do objeto str em maiúsculas
couser.lower()# método lower() retorna o valor do objeto str em minúsculas
couser.title()# método title() retorna o valor do objeto str em maiúsculas, mas com a primeira letra de cada palavra em maiúsculas
couser.capitalize()# método capitalize() retorna o valor do objeto str em maiúsculas, mas com a primeira letra em maiúsculas e o restante em minúsculas
couser.strip()# método strip() remove os espaços em branco do início e do fim do objeto str
couser.replace("Curso", "Aula")# método replace() substitui uma parte do objeto str por outra parte
couser.split()# método split() divide o objeto str em uma lista de strings, usando o espaço em branco como separador
couser.splitlines()# método splitlines() divide o objeto str em uma lista de strings, usando o caractere de nova linha como separador

print('Python' in couser) # verifica se a string "Python" está contida na variável couser
print('Python' not in couser) # verifica se a string "Python" não está contida na variável couser

print(couser.lower())
print(couser.upper())
print(couser.title())   
print(couser.capitalize())  
print(couser.strip())   
print(couser.replace("Curso", "Aula"))
print(couser.split())
print(couser.splitlines())



