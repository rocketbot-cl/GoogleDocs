# Google Docs
  
Modulo para controlar Google Docs  

*Read this in other languages: [English](Manual_GoogleDocs.md), [Português](Manual_GoogleDocs.pr.md), [Español](Manual_GoogleDocs.es.md)*
  
![banner](imgs/Banner_GoogleDocs.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Configurar credenciales G-Suite
  
Obtiene los permisos para manejar Google Docs con Rocketbot
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta archivo de credenciales|Seleccione el archivo de credenciales de G-Suite|Ruta|

### Nuevo documento
  
Crea nuevo documento Google Docs.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del documento|Nombre del documento a crear|Nombre: |
|Variable donde se guardará el ID|Variable donde se guardará el ID del documento creado|{Resultado}|

### Escribir en documento
  
Escribe sobre documento Google Docs
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ingrese Document ID|Ingrese el ID del documento de Google Docs|1XfKS0_ftXfKSpO_iX6udViX6udViX6udV_iX6udV|
|Escriba texto|Texto a escribir en el documento de Google Docs|Lorem ipsum dolor sit amet, consectetur adipiscing elit.|

### Leer documento
  
Lee un documento Google Docs
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del documento|ID del documento de Google Docs|1XfKS0_ftXfKSpO_iX6udViX6udViX6udV_iX6udV|
|Variable donde se guardará el resultado|Variable donde se guardará el resultado de la lectura del documento|{Resultado}|

### Agregar imagen
  
Agrega una imagen al documento
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del documento|ID del documento al cual se le agregará la imagen. El ID del documento se encuentra en la URL del documento|1XfKS0_ftXfKSpO_iX6udViX6udViX6udV_iX6udV|
|Url de la imagen|Url de la imagen que se agregará al documento|imagen.jpg|
