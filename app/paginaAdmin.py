#!C:\Users\zx21student030\AppData\Local\Programs\Python\Python310\python.exe
import sys
sys.path.append('../')

import os
from http import cookies
from modules.paginas import redireccion
import datetime
import json
from modules.paginas import admin

cookiesPagina = {}
usuarios = []

def completarTabla():
     cadena = ''
     for usuario in usuarios:
          cadena += """
               <tr>
                    <td class="columna-tabla">"""+usuario[0]+"""</td>
                    <td class="columna-tabla">"""+usuario[1]+"""</td>
                    <td class="columna-tabla">"""+usuario[3]+"""</td>
               </tr>
          """
     return cadena

if 'HTTP_COOKIE' in os.environ:
     listaCoki = os.environ['HTTP_COOKIE']
     listaCoki = listaCoki.split("; ")

     for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        cookiesPagina[nombre]=valor
    
if 'SID' in cookiesPagina:

     if os.path.isfile('./../data/usuarios.json'):
          file = open('./../data/usuarios.json', 'rt')
          usuarios = json.loads(file.read())
          file.close()

     print('Content-Type: text/html\n')
     tabla = completarTabla()
     print (admin.format(tabla))
else:
     print('Content-Type: text/html\n')
     print(redireccion.format(0, './../modules/error.html', '', ''))