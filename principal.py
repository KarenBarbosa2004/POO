class Coche:
    """ color="Rojo"
    marca="Ferari"
    modelo="Aventador"
    velocidad=300
    caballaje=500
    motor=2600"""
    #método constructor
    def __init__(self,color,marca,modelo,velocidad,caballaje,motor):
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.velocidad=velocidad
        self.caballaje=caballaje
        self.motor=motor
    
    
#métodos
    #def setColor(self,color):
    #    self.color=color
    def getColor(self):
        return self.color 
    # def setMarca(self,marca):
        # self.marca=marca
    def getMarca(self):
        return self.marca
    # def setModelo(self,modelo):
        #  self.modelo=modelo
    def getModelo(self):
        return self.modelo
    def acelerar(self):  
        self.velocidad+=1
    
    def frenar(self):    
        self.velocidad-=1
    def getVelocidad(self):
        return self.velocidad
    
    def getCaballaje(self):
        return self.caballaje
    def getMotor(self):
        return self.motor
    def obtenerInformacion(self):
        
        info="Información del Coche"
        info+="\n Color:"+self.getColor()
        info+="\n Marca:"+self.getMarca()
        info+="\n Modelo:"+self.getModelo()
        info+="\n Velocidad:"+str(self.getVelocidad())
        info+="\n Caballaje:"+str(self.getCaballaje())
        info+="\n Motor:"+str(self.getMotor())
        return info