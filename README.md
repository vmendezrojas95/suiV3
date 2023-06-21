# zuiV2

Descripción :

zuiV2 es un proyecto Django que busca simular el sistema de inscripción a carreras y materias utilizado por algunas instituciones educativas,
tomando como ejemplo el SIU GUARANI utilizado por IFTS 18. El proyecto incluye las aplicaciones "carrera", "curso", "docente", "estudiante" y "matricula", 
cada una con sus respectivos archivos de Django y una carpeta "templates" con los archivos HTML para las vistas.

Requisitos previos: ( Sujeta cambios)

Python 3.x
Virtualenv (opcional)


Instalación:

Clonar el repositorio: git clone https://github.com/vmendezrojas95/zuiV2
Navegar al directorio del proyecto: cd IFTSv2
Crear y activar un entorno virtual (opcional): virtualenv venv && source venv/bin/activate
Instalar las dependencias: pip install -r requirements.txt
Crear la base de datos: python manage.py migrate
Crear un superusuario: python manage.py createsuperuser
Ejecutar el servidor: python manage.py runserver


Uso:

Para acceder al sitio web, abrir un navegador y visitar http://localhost:8000
Para acceder al panel de administración, visitar http://localhost:8000/admin y utilizar las credenciales del superusuario creado en la instalación.


Estructura del proyecto:

IFTSv2/: Carpeta raíz del proyecto.
IFTSv2/apps/: Carpeta que contiene todas las aplicaciones del proyecto.
IFTSv2/apps/carrera/, IFTSv2/apps/curso/, IFTSv2/apps/docente/, IFTSv2/apps/estudiante/, IFTSv2/apps/matricula/: Aplicaciones con sus respectivos archivos de Django y una carpeta templates con los archivos HTML para las vistas.
IFTSv2/requirements.txt: Archivo necesario para instalar las dependencias del proyecto.


Contribución:

Crear un fork del repositorio.
Crear una rama para la nueva funcionalidad: git checkout -b nueva-funcionalidad
Realizar los cambios y confirmarlos: git commit -m "Nueva funcionalidad"
Empujar los cambios a la rama: git push origin nueva-funcionalidad
Crear un Pull Request en GitHub.
