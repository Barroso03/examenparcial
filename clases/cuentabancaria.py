class cuenta_bancaria():
    def _init_(self,operaciones,datos_bancarios):
       self.operaciones = operaciones
       self.datos_bancarios = datos_bancarios
    def operaciones(self,retirar,ingresar,transferir,saldo):
        self.saldo = saldo
        saldo = 10000
        self.retirar = retirar
        retirar = 78
        self.ingresar = ingresar
        ingresar = 575
        self.transferir = transferir
        transferir = 2000
        if retirar < saldo:
            print("No se puede retirar dinero")
        if transferir < saldo:
            print("No se puede retirar ingresar")
        else:
            print("Se puede realizar la operacion")
    def datos_bancarios(self,ID,nombre_titular,fecha_apertura,numero_cuenta):
        self.ID = ID
        ID = 123456789012
        self.nombre_titular = nombre_titular
        nombre_titular = ("Jorge Barroso") 
        self.fecha_apertura = fecha_apertura
        fecha_apertura = (17-12-2015)
        self.numero_cuenta = numero_cuenta
        numero_cuenta = (253695067352)
        print(ID)
        print(nombre_titular)
        print(fecha_apertura)
        print(numero_cuenta)
print(cuenta_bancaria.operaciones("78,575,2000,10000"))
print(cuenta_bancaria.datos_bancarios("123456789012,Jorge Barroso,17-12-2003,253695067352"))