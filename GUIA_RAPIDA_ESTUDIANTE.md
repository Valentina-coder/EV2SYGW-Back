# Guía rápida - MediConnect

## Requisitos

- Python 3.11 o superior
- Dependencias de `requirements.txt`

## Instalación y ejecución local (PowerShell)

```powershell
python -m pip install -r requirements.txt
$env:MEDICONNECT_RUT = "<RUT de prueba>"
$env:MEDICONNECT_PASSWORD = "<contraseña de prueba>"
$env:MEDICONNECT_TOKEN = "<token de prueba>"
uvicorn main:app --reload --host 0.0.0.0 --port 8080
```

El inicio de sesión requiere las tres variables de entorno indicadas. Si falta
alguna, el endpoint responde con código 503. No guardes credenciales ni tokens
en el código, archivos versionados o imágenes Docker.

## Docker

Pasa `MEDICONNECT_RUT`, `MEDICONNECT_PASSWORD` y `MEDICONNECT_TOKEN` al contenedor
en tiempo de ejecución mediante el mecanismo de secretos de tu entorno.

## SonarQube

Configura `SONAR_TOKEN` en el entorno desde donde ejecutes el análisis. El
scanner puede leer esta variable automáticamente; el token no debe guardarse
en `sonar-project.properties`.
