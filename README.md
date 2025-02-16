# Primera Entrega - Curso Python

## Descripción

Este es un proyecto desarrollado en Python utilizando el framework Django. Contiene una estructura organizada con archivos y carpetas esenciales para su funcionamiento.

## Estructura del Proyecto

```

- fotos/                # Carpeta para almacenar imágenes
- home/                 # Carpeta principal del proyecto
  - migrations/         # Carpeta que contiene las migraciones de los modelos
  - templates/          # Archivos HTML para la vista
  - forms.py            # Formularios de Django
  - models.py           # Definición de modelos de base de datos
  - views.py            # Lógica de las vistas
  - urls.py             # Definición de rutas
- proyecto/             # Carpeta con las configuraciones principales del proyecto
- templates/            # Carpeta global de templates (ej. base.html) Ahora no se esta usando pero la idea es luego heredar las configuraciones principales de esta carpeta.
- manage.py             # Archivo principal para ejecutar comandos Django
- initial_data.json     # JSON con datos iniciales de productos
- requirements.txt      # Lista de dependencias necesarias para el proyecto
- .gitignore            # Archivo para excluir archivos innecesarios del control de versiones

```

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/nicoalvarezmg/AlvarezNicolas-TuPrimeraPagina
cd AlvarezNicolas-TuPrimeraPagina
```

### 2. Crear un entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Instalar la base de datos de productos inicial

```bash
python manage.py loaddata initial_data.json
```

### 6. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

## Uso

Después de ejecutar el servidor, puedes acceder a la aplicación en tu navegador en la dirección:

```
http://127.0.0.1:8000/pipes-home/
```
