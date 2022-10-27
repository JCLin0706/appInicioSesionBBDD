#!C:\Users\zx21student030\AppData\Local\Programs\Python\Python310\python.exe
import sys
sys.path.append('../')

import os
from modules.paginas import redireccion
from http import cookies
import datetime

todasCokis={}

if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE']
    listaCoki = listaCoki.split("; ")

    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCokis[nombre]=valor

if 'SID' in todasCokis:
    coki = cookies.SimpleCookie()
    coki["SID"]=todasCokis["SID"]
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=-1)
    coki['SID']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
    print(coki)
    print('Content-Type: text/html\n')
    print(redireccion.format(0, './../appInicioSesion.html', '', ''))
else:
    print('Content-Type: text/html\n')
    print(redireccion.format(3, './../modules/error.html', '', ''))