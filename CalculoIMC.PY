Peso=float(input("Ingresa TU Peso: "))
Estatura=float(input("Ingrresa TU Altutra: "))
imc=(Peso/(Estatura**2))
print ("TU Indice de Masa Corporal Es: "+str (imc))

if (imc>=18.5 and imc<=24.9 ):

 print ("Saludable")   

if (imc<18.5 ):

 print ("BAJO DE PESO")   
if (imc>=25 and imc<=29.9 ):

 print ("Sobre Peso")   

if (imc>30 ):

  print ("Obesidad")   
 