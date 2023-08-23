def cosa(num3,num2):
    
    print(num3+num2)
    

def comparador(algo1,algo2):

 if algo1 > algo2:
    
    print("el primer valor es el más grande")
    
 else:
    
    print("el segundo valor es el más grande")




comparador(2,3)


def interes_simple(valor_inicial,interes,periodos):
    
    print((valor_inicial*(interes/100)*periodos)+valor_inicial)
    

interes_simple(100000,5,3)





def pulgadas(centimetro):
    
    print(centimetro*0.393701)
    
pulgadas(1)

pulgadas(60)
    
lado= float (input("¿cuanto mide el lado?"))
respuesta=lado**3
    
print("el volumen es", respuesta)
    
    
    
tiempo=int(input("Introduce la cantidad de segundos"))

hora=tiempo//3600

minutos_sin_dividir=tiempo%3600

minutos=minutos_sin_dividir//60

segundos=minutos_sin_dividir%60

print("equivalen",hora,"horas ,",minutos,"minutos y",segundos,"Segundos")

nombre=(input("¿what is your name?"))
año=int(input("introduce el año de nacimiento "))

mes=int(input("introduce el munero del mes de nacimiento"))

dias=int(input("introduce el numero del mes en el que naciste"))

años=2023-año

meses=8-mes

dia=17-dias

if meses<0:

 meses=meses+12





if dia<0:

 dia=dia+31
 

print(nombre,"tu tienes", años," años ,", meses, " meses y", dia, "dias" )

pulgada=float(input("ingresa la cantidad de pulgadas"))

centimetro=pulgada*2.54

print("son",centimetro, "centimetros")



centimetros=float(input("ingresa la cantidad de pulgadas"))

pulgadas=centimetros*0.393701

print("son",pulgadas, "pulgadas")

    
    

 






