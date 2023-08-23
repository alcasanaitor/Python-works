#Problema 1#

num1=float(input("ingresa el primer numero para calcular el promedio con tres numeros"))
num2=float(input("ingresa el segundo numero para calcular el promedio con tres numeros"))
num3=float(input("ingresa el tercer numero para calcular el promedio con tres numeros"))

prom=((num1+num2+num3)/3)

print("el promedio de los tres numeros que ingreso es ,",prom )

#Problema 2#

numero=float(input("ingrese el numero al que quiere sacarle raiz"))
raiz=float(input("elija la raiz la cual quiere aplicarle al numero que escogio"))

resultado=numero**(1/raiz)

print(" el resultado de su operacion matematica es", resultado)

#problema 3#

pulgadas=float(input("ingresa el numero de pulgadas que quieres convertir a pies y pulgadas"))

pies=pulgadas//12

pulgadas_sobrantes=pulgadas%12

print("la medida es",pies, "pies y", pulgadas_sobrantes, " pulgadas")

#problema 4#

tiempo=int(input("Introduce la cantidad de segundos"))

hora=tiempo//3600

minutos_sin_dividir=tiempo%3600

minutos=minutos_sin_dividir//60

segundos=minutos_sin_dividir%60

print("la cantidad de segundos que ingreso equivalen a ",hora,"horas ,",minutos,"minutos y",segundos,"Segundos")

#problema 5#

nuditos=float(input("introduce la cantidad de nudos para convertir a kilometros por segundo"))

kilometros_por_segundo= nuditos*1.854

print("la cantidad de", nuditos," nudos equivale a",kilometros_por_segundo,"kilometros por segundo")

#problema 6#

galones=float(input("introduce la cantidad de galones de cerveza consumidos "))

galones_en_cc=galones*3785.41

botellas=galones_en_cc//330

print("se han consumido en galones o equivalente a",botellas, " botellas de 330cc" )

#Problema 7#

saco=int(input("cuantos sacos tenis pa vender po"))

total_kilos=saco*60

almud=total_kilos//9

kilos_sobrantes=total_kilos%9

ganancia=almud*3500

print(" en total teni", almud, "almud con lo que ganaras ", ganancia,  "pesos, buena plata po,pero pero te sobran", kilos_sobrantes, "kilos, te recomiendo po que encotri la forma en que los vendai po" )


#Problema 8#

piso=float(input("¿cuantos metros cuadrados quieres cubrir con tablas?"))

ancho=float( input("introduce el ancho de las tablas en pulgadas"))

largo=float( input("introduce el largo de las tablas en centimetros"))

ancho_tabla=ancho*2.54

piso_centimetros_cuadrados=piso*10000

tabla=ancho_tabla*largo

tablas_totales=piso_centimetros_cuadrados/tabla

divisor_si=piso_centimetros_cuadrados//tabla

if tablas_totales>divisor_si:
    
   tablas_totales=divisor_si+1
   
else:
    
    tablas_totales=divisor_si
           

print("se necesitan por lo menos", tablas_totales, "tablas en total para cubrir el piso")

   