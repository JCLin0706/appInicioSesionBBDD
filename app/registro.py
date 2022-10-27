#!C:\Users\zx21student030\AppData\Local\Programs\Python\Python310\python.exe
import sys
sys.path.append('../')

import os
import cgi
import json
from modules.paginas import redireccion
import hashlib

args = cgi.parse()
datos = []


def obtenerDatos():
     datos.append(args["nombre"][0])
     datos.append(args["correo"][0])
     h = hashlib.sha512(str.encode(args["contrasena"][0]))
     datos.append(h.hexdigest())
     datos.append('user')

def guardarDatosFichero():
     if os.path.isfile('./../data/usuarios.json'):
          file = open('./../data/usuarios.json', 'rt')
          usuariosJson = json.loads(file.read())
          file.close()
          usuariosJson.append(datos)
     else:
          usuariosJson = []
          usuariosJson.append(datos)
          
     file = open('./../data/usuarios.json', 'wt')
     file.write(json.dumps(usuariosJson))
     file.close()

def datosCorrectos():
     for dato in datos:
          if dato == '':
               return False
     
     return True

def comprobarRepetidos():
     if os.path.isfile('./../data/usuarios.json'):
          file = open('./../data/usuarios.json', 'rt')
          usuariosComprobar = json.loads(file.read())
          file.close()
          
          for usuario in usuariosComprobar: 
               if (usuario[0] == datos[0]) or (usuario[1] == datos[1]):
                         return False
          return True
     else:
          return True
     
if len(args)== 3 and ("nombre" in args and "correo" in args and "contrasena" in args):
     
     obtenerDatos()
     
     if datosCorrectos() and comprobarRepetidos():
          guardarDatosFichero()
          print("Content-Type: text/html\n")
          print(redireccion.format(0, './../appInicioSesion.html', '', ''))
     else:
          print("Content-Type: text/html\n")
          print(redireccion.format(0, './../modules/error.html', '', ''))
               
else:
     print("Content-Type: text/html\n")
     print(redireccion.format(0, './../modules/error.html', '', ''))