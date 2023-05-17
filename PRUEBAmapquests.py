#Importamos las librerias necesarias para trabajar
import urllib.parse
import requests
import json
bucle = True
i = "galleta"
while bucle == True:
    main_api = "https://www.mapquestapi.com/directions/v2/route?" #url principal, esta sera la base del link que formaremos junto con el origen y destino
    orig = input(str("Inserte la cuidad de origen: ")) #Le pedimos al usuario por la cuidad de origen del viaje
    dest = input(str("Inserte la cuidad de destino: ")) #Pedimos tambien la cuidad de destino
    idioma = "es_MX"
    key = "Ec80kmCjC6BEZDMV5KIp9gBNHvT0Ez6M" #Insertamos la key de la cuenta de mapquest developer
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest,"locale":idioma}) #Aca formamos el link la key y las cuidades de origen y destino

    data = requests.get(url).json() #Extraemos el archivo .json con el link ya formado

    distancia = (data['route']['distance']) #Metemos el valor de la distancia en una variable
    distancia_km = round(distancia*1.609, 1) #Para cambiar la distancia de millas a kilometros multiplicamos por 1,609, ademas redondeamos el resultado con solo un decimal

    tiempo = (data['route']['time']) #Metemos el valor del tiempo en una variable
    tiempohoras = (tiempo//3600)
    tiempomin= ((tiempo % 3600) // 60)
    tiemposeg= (tiempo % 60)


    recorrido = (data['route']['legs'][0]['maneuvers'])


    #print("Link del mapa: ", url) #Esta linea se uso durante las pruebas para ver de donde sacar los datos :)
    print("------La distancia total a recorrer es de: ", distancia_km, "Kilometros------")
    print("------El tiempo de viaje es de: ", int(tiempohoras), "Horas", int(tiempomin), "Minutos y ", int(tiemposeg), "segundos------")
    for step in recorrido:
        print("* ", step["narrative"])
    i = input(str("Para continuar el programa ponga cualquier caracter, de lo contrario ponga S, s o salida : "))
    if i == "S":
        print("Terminando programa :(")
        quit()
    elif i == "s": 
        print("Terminando programa :(")
        quit()
    elif i == "salida":
        print("Terminando programa :(")
        quit()
    else :
        print("Ok :)")