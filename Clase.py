class Persona:
    """
    nombre
    apellidos
    altura
    edad
    """
    #Métodos getter
    def getNombre(self):
        return self.nombre
    def getApellidos(self):
        return self.apellidos
    def getAltura(self):
        return self.altura
    def getEdad(self):
        return self.edad
    #Métdos setter
    def setNombre(self,nombre):
        self.nombre=nombre
    def setApellidos(self,apellidos):
        self.apellidos=apellidos
    def setAltura(self,altura):
        self.altura=altura
    def setEdad(self,edad):
        self.edad=edad
        #metodos hablar,caminar,dormir
    def hablar(self):
        return "Estoy hablando"
    def caminar(self):
        return "Estoy caminando"
    def dormir(self):
        return "Estoy durmiendo"
#implementar la herencia , creo la clase informaico que hereda de persona   
class Informatico(Persona):
    """
    lenguajes
    experiencia
    """
    #método constructor
    def __init__(self):
        self.lenguajes="HTML. CSS,JAVASCRIPT,PHP"
        self.experiencia=5   
        #métodos getter   
    def getLenguajes(self):
        return self.lenguajes
    def getExperiencia(self):
        return self.experiencia
    #métodos aprender,programar
    def aprender(self,lenguajes):
        set.lenguajes=lenguajes
        return self.lenguajes
    def programar(self):
        return "Estoy programando"
    def repararPc(self):
        return("He reparado tu Pc")
class TecnicoRedes(Informatico):
    #método constructor de la clase hija TecnicoRedes
    def __init__(self):
        super().__init__()
        self.auditoriaRedes='experto'
        self.experienciaredes=10
        
    def getAuditoriaredes(self):
        #set.auditoriaRedes=auditoriaRedes
        return self.auditoriaRedes
    def getExperienciaredes(self):
        #set.auditoriaRedes=auditoriaRedes
        return self.experienciaredes
    
    def auditar(self):
        return "Estoy auditando una red"