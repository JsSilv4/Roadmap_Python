#operadores aritmeticos
#suma, resta, multiplicacion, division, division entera, modulo, exponencial

a = 10
b = 5

suma = a + b #suma
subtracao = a - b #subtracao
multiplicacion = a * b #multiplicacion
division = a / b #division
division_entera = a // b #division entera
modulo = a % b #modulo
exponencial = a ** b #exponencial
a += 1 #incremento
b -= 1 #decremento
a *= 2 #multiplicacion

print(suma, subtracao, multiplicacion, division, division_entera, modulo, exponencial)

#operador de precedencia

#1. Parentesis
#2. Exponencial
#3. Multiplicacion y division
#4. Suma y resta
#5. Comparacion
#6. Asignacion
#7. Logicos
#8. Identidad
#9. Membresia
#10. Identidad

x = 10 + (5 + 2) ** 2
print(x) 

#operador de comparacion
#==, !=, >, <, >=, <=                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
3 == 3 #igual
3 != 4 #diferente
3 > 2 #mayor
3 < 4 #menor
3 >= 3 #mayor o igual
3 <= 4 #menor o igual

#operador logico
#and, or, not
2 > 1 and 3 < 4 #and
2 > 1 or 3 < 4 #or
not 2 > 1 #not

#operador de bit
#&, |, ^, ~, <<, >>
2 & 3 #and
2 | 3 #or
2 ^ 3 #xor
~2 #not
2 << 3 #desplazamiento a la izquierda
2 >> 3 #desplazamiento a la derecha

#operador de identidad
#is, is not
2 is 2 #is
2 is not 3 #is not 

#operador de membresia
#in, not in
2 in [1, 2, 3] #in
2 not in [1, 2, 3] #not in

