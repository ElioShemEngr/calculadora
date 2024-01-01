#Crear Calculadora en Python

# Crear Variables
print('Ingrese los valores a operar')

num1 = int(input('Primer Valor: '))
num2 = int(input('Segundo Valor: '))

print('Ingrese operador +, -, *, /')
operador = input('>>  ')

resultado = 0

if operador == '+':
  resultado = num1 + num2
elif operador == '-':
  resultado = num1 - num2
elif operador == '*':
  resultado = num1 * num2
elif operador == '/':
  resultado = num1 / num2
else:
  print(f'Operador {operador} no reconocido')

print(f"El Resultado es : {resultado}")
