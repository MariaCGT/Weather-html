#coding:utf-8
import json
import requests
import webbrowser	
from jinja2 import Template


def direccion_viento(cadena):
	if cadena >= 337.5 or cadena >=0 and cadena < 22.5:
		return "N"
	if cadena >= 22.5 and cadena < 67.5:
		return "NE"
	if cadena >= 67.5 and cadena < 112.5:
		return "E"
	if cadena >= 112.5 and cadena < 157.5:
		return "SE"
	if cadena >= 157.5 and cadena < 202.5:
		return "S"
	if cadena >= 202.5 and cadena < 247.5:
		return "SO"
	if cadena >= 247.5 and cadena < 292.5:
		return "O"
	if cadena >= 292.5 and cadena < 337.5:
		return "NO"
	

lista_ciudades = ('Almeria','Cadiz','Cordoba','Huelva','Jaen','Malaga','Sevilla')

f = open('plantillah.html','r')
f_html = open('weather.html','w')
html = ''
temp_min = []
temp_max = []
veloc_viento = []
direc_viento = []
provincia = []


for elemento in lista_ciudades:
	provincia.append(elemento)
	respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather?',params={'q':'%s,spain' %elemento})
	diccionario_json = json.loads(respuesta.text)
	temp_min.append(int(diccionario_json["main"]["temp_min"] - 273))
	temp_max.append(int(diccionario_json["main"]["temp_max"] - 273))
	veloc_viento.append(int(diccionario_json["wind"]["speed"]*1.6))
	direc_viento.append(direccion_viento(diccionario_json["wind"]["deg"]))
	print elemento
for linea in f:
	html += linea

plant_template = Template(html)

salida_html = plant_template.render(lista_ciudades = provincia, temperatura_minima = temp_min, temperatura_maxima = temp_max, viento_velocidad = veloc_viento, viento_direccion = direc_viento)

f_html.write(salida_html)

webbrowser.open("weather.html")

	




