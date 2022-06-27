import cuenta
#objetos
print('\n|Cuenta|')
cuenta1=cuenta.Cuenta(1234567890,'25/octubre/2019',1000000)
print(cuenta1.retiro())
print(cuenta1.consignar())
print(cuenta1.informacion())
print("--------------------------------------------------------------------------")
print("|Cuenta corriente|")
corriente1=cuenta.cuentaCorriente(9876543322,'14/febrero/2020',2000000,9080)
print(corriente1.retiro())
print(corriente1.consignar())
print(corriente1.informacion())
print(corriente1.corriente())