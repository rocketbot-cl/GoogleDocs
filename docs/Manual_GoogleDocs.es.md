# Google Docs
  
Modulo para controlar Google Docs  

*Read this in other languages: [English](Manual_GoogleDocs.md), [Português](Manual_GoogleDocs.pr.md), [Español](Manual_GoogleDocs.es.md)*
  
![banner](imgs/Banner_GoogleDocs.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Como usar este modulo

Antes de usar este modulo, es necesario registrar tu aplicación en el portal de Google Cloud. 

1. Ingresar con una cuenta de google al siguiente link: https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard
2. Completar el formulario y luego presionar Crear
3. Dentro del Menu de Navegación (Izquierdo), ingresar en API y Servicios
4. En la sección superior, ingresar a "+ HABILITAR API Y SERVICIOS"
5. Buscar "Google Docs API", seleccionar y por ultimo habilitar
6. Nuevamente dirigirse a Menu de Navegación (Izquierdo) > API y Servicios > Credenciales
7. Presionar el botón "Configurar pantalla de consentimiento". En User type elegir de lo posible "Interno". Si no está disponible, deberás seleccionar "Externo" y completar los campos obligatorios.
8. Completar los campos requeridos con la información de tu aplicación y presionar Guardar y continuar.
9. En el paso 2, haz click en "Agregar o quitar permisos", filtra "Google Docs API", marca todos los permisos y presiona Actualizar. Luego presiona Guardar y continuar.
10. Vuelve a "Credenciales"
11. Presiona Crear Credenciales > ID de cliente de OAuth, seleccionar como Tipo de Aplicación: App de Escritorio, colocar un nombre y crear.
12. Descargar el archivo JSON de credenciales.
13. Si la aplicación fue creada como "Externo", debe dirigirse a Menu de Navegación (Izquierdo) > Pantalla de Consentimiento y agregar usuario dentro de la seccion "Usuarios de prueba"


## Descripción de los comandos

### Configurar credenciales G-Suite
  
Obtiene los permisos para manejar Google Docs con Rocketbot
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta archivo de credenciales|Seleccione el archivo de credenciales de G-Suite|Ruta|
|Asignar resultado a variable|Asigna el resultado de la conexión a una variable|resultado|

### Nuevo documento
  
Crea nuevo documento Google Docs.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del documento|Nombre del documento a crear|Nombre: |
|Variable donde se guardará el ID|Variable donde se guardará el ID del documento creado|resultado|

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
|Variable donde se guardará el resultado|Variable donde se guardará el resultado de la lectura del documento|resultado|

### Agregar imagen
  
Agrega una imagen al documento
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del documento|ID del documento al cual se le agregará la imagen. El ID del documento se encuentra en la URL del documento|1XfKS0_ftXfKSpO_iX6udViX6udViX6udV_iX6udV|
|Url de la imagen|Url de la imagen que se agregará al documento|https://example.com/image.jpg|
