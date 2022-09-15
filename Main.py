from Empleado import Empleado
from Cliente import Cliente

# emp = Empleado('1010119993','Manuel', 'Ortega', ' 3044620556', 'calle9-19-73', 1000)
# cli = Cliente('1010119993','Manuel', 'Ortega', '3044620 3044620556', 'calle9-19-73', 'vip')

# print(emp)
# print(cli)
PersonalEmpresa = []
def cargar():
    respuesta = input('Es usted un Empleado?')
    cedula = input('Cedula:')
    nombre = input('Nombre:')
    apellido = input('Apellido:')
    direccion = input('Direccion:')
    telefono = int(input('Telefono:'))
    if(respuesta == 'si'):
        salario = int(input('Salario:'))
        emp = Empleado(cedula, nombre, apellido, direccion, telefono, salario)
        PersonalEmpresa.append(emp)
    else:
        categoria = input('Categoria:')
        clie = Cliente(cedula, nombre, apellido, direccion, telefono, categoria)
        PersonalEmpresa.append(clie)

print('Cantidad de persona a ingresar')
n = int(input())
for i in range(n):
    cargar()
for j in PersonalEmpresa:
    print(j)
