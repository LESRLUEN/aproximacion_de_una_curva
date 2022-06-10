#importamos a sympy como sp
import sympy

#Declaramos los símbolos que usaremos
from sympy import integrate

x, y = sympy.symbols('x y')



#Utilizamos el método init_printing
sympy.init_printing(use_unicode=True)

b= int(input('Ingrese Coeficiente de X = '))
n= int(input('Ingrese Numerador = '))
d= int(input('Ingrese Denominador = '))


res= sympy.diff(b*(x)**(n/d), x)

print(res)
print('  ')

print('Integrales Definidas')

#f=input(' Ingrese la funcion definida f=')
g= res
f=sympy.sqrt((1+((g)**2)))

#x=symbols('x')

#f=x**3+3*x**2-2*x-1

x0=input('Ingrese el limite inferior x0=')
x1=input('Ingerese el limite superior x1=')

resp=integrate(f,(x,x0,x1))
print(' ')
print(f'El resultado es {resp}'))