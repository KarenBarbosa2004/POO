class Cuenta:
#atributos: numero, fecha apertura, saldo. en constructor.
    def __init__(self,numero,fecha_apertura,saldo):
        self.numero = numero
        self.fecha_apertura = fecha_apertura
        self.saldo = saldo

#metodo Retiro
    def retiro(self):
        print("--------------------------------------------------------------------------")
        while True:
            self.retiro=int(input(f'Digite el valor a retirar |su saldo total es de -->  {self.saldo}| : '))
            if self.saldo>=self.retiro:
                self.saldo-=self.retiro
                return f'Su retiro ha sido ¡Exitodo! --> Saldo Total {self.saldo}'
            else:
                print('El valor que desea retirar es insuficiente')
                continue

#metodo consignar
    def consignar(self):
        print("--------------------------------------------------------------------------")
        self.consignar=int(input(f'Digite el valor a consignar |su saldo total es de --> {self.saldo}|: '))
        if self.consignar>0:
            self.saldo+=self.consignar
            return f'Su consigna ha sido ¡Exitosa! --> {self.saldo}'

#informacion de la cuenta
    def informacion(self):
            print("--------------------------------------------------------------------------")
            return('Número de cuenta: {}\nFecha de apertura: {}\nSaldo total: {}'.format(self.numero,self.fecha_apertura,self.saldo))

#clase hija llamada cuentaCorriente, con su atrubuto denominado cheque
class cuentaCorriente(Cuenta):
    def __init__(self, numero, fecha_apertura, saldo,cheque):
        super().__init__(numero, fecha_apertura, saldo)
        self.cheque=cheque
    def corriente(self):
        return('Número de cheque: {}'.format(self.cheque))