#Inmobiliaria 
#Lista de Inmuebles 

#Aca se crea un diccionario que dentro de el hay una lista y dentro de la lista vuelve a ver un diccionario. 
Lista_de_Inmuebles = {'Inmuebles':[  {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'}, 
                                    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},    
                                    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'}, 
                                    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B' }, 
                                    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]}


presupuesto=float(input("Oiga que plata tiene: "))


for i in range (len(Lista_de_Inmuebles["Inmuebles"])):
        print(Lista_de_Inmuebles["Inmuebles"][i])






