## Conversão de Tipos
# Conversão de tipos é o processo de transformar um valor de um tipo de dado para outro tipo de dado.
# Em Python, existem várias funções embutidas que podem ser usadas para conversão de tipos, como:
# int(), float(), str(), bool(), etc.

data_Nasc = input("Qual sua data de nascimento? ")
idade = 2024 - int(data_Nasc) #data_Nasc é uma string, então está convertendo para inteiro # A função int() converte a string para um número inteiro.
print(f"Você nasceu em {data_Nasc} e tem {idade} anos.")

# exemplo de conversão de float para int
# A função int() converte um número float para um número inteiro, truncando a parte decimal.

float_num = 3.14
int_num = int(float_num) 
print(f"Float: {float_num}, Int: {int_num}")

# declarando o type diretamente na linha de entrada
Firts = int(input("Digite o primeiro número: "))
Second = int(input("Digite o segundo número: "))
print(f"A soma de {Firts} e {Second} é {Firts + Second}.")


Firts = 3.14
Second = 20
result = Firts + float(Second) # A função float() converte o inteiro para um número float.
print(f"A soma de {Firts} e {Second} é {result}.")

# exemplo de conversão de str para bool
# A função bool() converte uma string para um valor booleano.
str_value = "True"
bool_value = bool(str_value) # A string "True" é convertida para True.
print(f"String: {str_value}, Bool: {bool_value}")


n1 = 20.00
n2 = 10
calc = n1 + int(n2)
print(f"A soma de {n1} e {n2} é {calc}.")
