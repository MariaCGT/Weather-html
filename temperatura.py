import json
import requests
#coding:utf-8

opciones = """
1. Almeria
2. Cadiz
3. Cordoba
4. Granada
5. Huelva
6. Jaen
7. Malaga
8. Sevilla
"""

dicc_ciudades = {'1':'Almeria','2':'Cadiz','3':'Cordoba','4':'Granada','5':'Huelva','6':'Jaen','7':'Malaga','8':'Sevilla'}

print opciones

print "De que ciudad quieres saber la temperatura actual (indica el numero)"

num_ciud = raw_input()

#ciudad = dicc_ciudades[num_ciud]

respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' %dicc_ciudades[num_ciud]})

print respuesta

#json.loads(respuesta)

#temp =  int(dicc_resp["main"]["temp"]) - 273

#print "La temperatura actual de %s es %n grados centigrados" % (ciudad,temp) 





