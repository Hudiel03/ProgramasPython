alumno= str(input("ingresa Nombre del Alumno:"))
m1=float(input("ingresa la calificacion de METODOLOGIA: "))
m2=float(input("ingresa la calificacion de ALGEBRA: "))
m3=float(input("ingresa la calificacion de CALCULO: "))
m4=float(input("ingresa la calificacion de ECONOMIA: "))
m5=float(input("ingresa la calificacion de ESTADISTICA: " ))
m6=float(input("ingresa la calificacion de ESTUDIO DE TRABAJO: "))

Promedio=((m1+m2+m3+m4+m5+m6)/6)
print ("El Promedio de "+str (alumno)+" Es: "+ str(Promedio))

if (Promedio >=7.0):
    
    
    print ("APROBADO")   

if (Promedio <=6.9):
       print ("REPROBADO") 


  