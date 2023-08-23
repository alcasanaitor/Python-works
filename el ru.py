digito_1=int(input("ingresa el primer digito del Rut"))
digito_2=int(input("ingresa el segundo digito del Rut"))
digito_3=int(input("ingresa el tercer digito del Rut"))
digito_4=int(input("ingresa el cuarto digito del Rut"))
digito_5=int(input("ingresa el quinto digito del Rut"))
digito_6=int(input("ingresa el sexto digito del Rut"))
digito_7=int(input("ingresa el septimo digito del Rut"))
digito_8=int(input("ingresa el octavo digito del Rut"))


A = [[digito_1,digito_2,digito_3],digito_4,digito_5,digito_6,digito_7,digito_8]


for row in A:
    
  for element in A:
     
    n1=digito_1*element
 
  for element in A:
     
    n2= digito_2*element

  for element in A:
     
    n3= digito_3*element
     
  for element in A:
     
    n4= digito_4*element
     
  for element in A:
     
     n5=digito_5*element
      
  for element in A:
     
     n6=digito_6*element
     
  for element in A:
     
     n7=digito_7*element
     
  for element in A:
     
    n8= digito_8*element
    
    
todo=n1+n2+n3+n4+n5+n6+n7+n8

modulo=todo//11

entero=modulo*11

calculo=entero-todo

if calculo==10:

 calculo=str("k")
 
elif calculo==11:
    
    calculo=0
    
else:
    
    calculo=calculo
    
    
    
print("el digito verificador es", calculo)
    
    
    


     

     
