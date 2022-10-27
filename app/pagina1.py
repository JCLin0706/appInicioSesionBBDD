#!C:\Users\zx21student030\AppData\Local\Programs\Python\Python310\python.exe
import sys
sys.path.append('../')

import os
from http import cookies
from modules.paginas import redireccion
import datetime
from modules.paginas import paginaInicioSesion

cookiesPagina = {}

if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE']
    listaCoki = listaCoki.split("; ")

    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        cookiesPagina[nombre]=valor
    
if 'SID' in cookiesPagina:
    print('Content-Type: text/html\n')
    print (paginaInicioSesion.format(cookiesPagina['SID'], '1', './../app/pagina2.py', '2'))
else:
    print('Content-Type: text/html\n')
    print(redireccion.format(0, './../modules/error.html', '', ''))