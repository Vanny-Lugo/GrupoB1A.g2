class Laboratorio:#clase

    #Métodos 
    def _init_(self,nota,aprendizaje):
        self.nota = nota
        self.aprendizaje= aprendizaje
        print ('Formando ingeniera')

    def Profesor(self,homeroortega):
        self.homeroortega= homeroortega
        print ('Homero Ortega')  

    
    def Lugar(self,lugar):
        self.lugar= lugar
        print ('Aula virtual')      
        
comunicaciones = Laboratorio() #Objeto
print(comunicaciones.Profesor)
print(comunicaciones.Lugar)





