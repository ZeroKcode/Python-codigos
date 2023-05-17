#Importamos las librerias necesarias para trabajar
import urllib.parse
import requests
import json
bucle = True #Creamos una variable para iniciar el bucle
i = "galleta" #Creamos una variable i que usaremos al final del codigo para preguntar si se desea o no seguir el bucle
while bucle == True: #Empezamos el bucle
    main_api = "https://www.mapquestapi.com/directions/v2/route?" #url principal, esta sera la base del link que formaremos junto con el origen y destino
    orig = input(str("Inserte la cuidad de origen: ")) #Le pedimos al usuario por la cuidad de origen del viaje
    dest = input(str("Inserte la cuidad de destino: ")) #Pedimos tambien la cuidad de destino
    idioma = "es_MX" #Definimos el idioma de salida como español
    key = "Ec80kmCjC6BEZDMV5KIp9gBNHvT0Ez6M" #Insertamos la key de la cuenta de mapquest developer
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest,"locale":idioma}) #Aca formamos el link la key y las cuidades de origen y destino

    data = requests.get(url).json() #Extraemos el archivo .json con el link ya formado

    distancia = (data['route']['distance']) #Metemos el valor de la distancia en una variable
    distancia_km = round(distancia*1.609, 1) #Para cambiar la distancia de millas a kilometros multiplicamos por 1,609, ademas redondeamos el resultado con solo un decimal

    tiempo = (data['route']['time']) #Metemos el valor del tiempo en una variable
    tiempohoras = (tiempo//3600) #Para el tiempo en horas dividimos en los segundos que hay en una hora y dejamos fuera el sobrante de la division
    tiempomin= ((tiempo % 3600) // 60) #Para los minutos hacemos lo mismo de antes pero dejando el sobrante, para poder dividir por 60 segundos y ahi si dejamos el sobrante fuera
    tiemposeg= (tiempo % 60) #Finalmente para los segundos simplemente dividimos en 60

    recorrido = (data['route']['legs'][0]['maneuvers']) #Metemos la informacion del recorrido en una variable


    #print("Link del mapa: ", url) #Esta linea se uso durante las pruebas para ver de donde sacar los datos :)
    print("------La distancia total a recorrer es de: ", distancia_km, "Kilometros------") #mostramos la distancia el kilometros con print
    print("------El tiempo de viaje es de: ", int(tiempohoras), "Horas", int(tiempomin), "Minutos y ", int(tiemposeg), "segundos------") # Mostramos tambien la duracion del tiempo en horas, minutos y segundos
    for step in recorrido:  #Ahora creamos un ciclo for para recorrer todos los pasos del recorrido
        print("* ", step["narrative"]) #Y mostramos cada paso del recorrido ordenadamente
    i = input(str("Para continuar el programa ponga cualquier caracter, de lo contrario ponga S, s o salida : ")) #Pedimos que se inserte in valor en la variable i para comparar en un condicional if/elif/else
    if i == "S": #Si "i" es igual a "S" entonces:
        print("Terminando programa :(") #Mostramos un mensaje de que se termina el programa
        quit() #Y terminamos el programa completo
    elif i == "s": #Repetimos pero con "s"
        print("Terminando programa :(") #nuevamente mostramos el mensaje de terminacion
        quit() #Matamos el programa
    elif i == "salida": #Repetimos con "salida"
        print("Terminando programa :(") #Una vez mas el mensaje de terminacion
        quit() #Y lo matamos
    else : #En caso de que las demas condiciones no se hayan complido seguimos con el programa normalmente
        print("Ok, siguiendo con el programa :)") #Impromimos un pequeño mensaje para indicar que seguiremos en el programa
