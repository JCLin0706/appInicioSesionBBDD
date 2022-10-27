paginaInicioSesion = """
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        
        <title>Inicio de Sesion</title>

        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400;0,600;0,700;0,800;1,700;1,800&display=swap" rel="stylesheet">

        <link rel="stylesheet" href="./../style/style.css">
    </head>

    <body>
        <header class="cabecera">
            <h3 class="titulo">Zoo de Madrid</h3>
        </header>
        <div class="contenido">
            <div class="contenedor-titulo">
                <h1 class="titulo">Bienvenido - {}<br>Pagina {}</h1>
            </div>
            <a href="{}" class="enlace-volver">Acceder a la Pagina {}</a>
            <a href="./../app/logout.py" class="enlace-volver">Logout</a>
        </div>


    </body>

    </html>
"""

admin = """
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        
        <title>Inicio de Sesion</title>

        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400;0,600;0,700;0,800;1,700;1,800&display=swap" rel="stylesheet">

        <link rel="stylesheet" href="./../style/style.css">
    </head>

    <body>
        <header class="cabecera">
            <h3 class="titulo">Zoo de Madrid</h3>
        </header>
        <div class="contenido">
          <div class="contenedor-titulo">
               <h1 class="titulo">El Zoo de Madrid</h1>
          </div>
          <table class="tabla">
               <tr>
                    <th class="columna-tabla nombre-columna-tabla">Nombre</th>
                    <th class="columna-tabla nombre-columna-tabla">Correo</th>
                    <th class="columna-tabla nombre-columna-tabla">Rol</th>
               </tr>
               {}
          </table>
          <a href="./../app/logout.py" class="enlace-volver">Logout</a>
        </div>

    </body>

    </html>
"""

redireccion = """<html lang="en">

<head>
     <meta charset="UTF-8">
     <meta http-equiv="X-UA-Compatible" content="IE=edge">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <meta http-equiv="refresh" content="{}; url={}">
     
     <title>Inicio de Sesion</title>

     <link rel="preconnect" href="https://fonts.googleapis.com">
     <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
     <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400;0,600;0,700;0,800;1,700;1,800&display=swap" rel="stylesheet">

     <link rel="stylesheet" href="./../style/style.css">
</head>

<body>
     <header class="cabecera">
          <h3 class="titulo">Zoo de Madrid</h3>
     </header>
     <div class="contenido">
          <div class="contenedor-titulo">
               <h1 class="titulo">Redirigiendo {}...</h1>
          </div>
          <p class="precio">{}</p>
     </div>


</body>

</html>
"""