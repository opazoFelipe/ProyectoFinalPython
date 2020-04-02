# Plataforma Web de Gestión de Apiarios

El proyecto presente en este repositorio corresponde a una plataforma web enfocada en la gestión de Apiarios, colmenas, apicultores y todos los componentes que estos contienen. 

## Comenzando

El proyecto se encuentra almacenado en el repositorio: 

```
http://gitlabtrans.face.ubiobio.cl/tddfelipebenjamin/apicultoresrdd
```

Para poder adquirir una copia, tan solo es necesario tener instalado git y realizar el comando:

```
git clone http://gitlabtrans.face.ubiobio.cl/tddfelipebenjamin/apicultoresrdd
```

Opcionalmente, se pueden descargar directamente desde la página web del repositorio.

### Prerequisitos

#### Con Docker

En el caso de que el proyecto se ejecute usando el Dockerfile encontrado en la carpeta 'dockerFileMysql', los requerimientos serían:

-Docker 19.03.8 o superior.

El Dockerfile descargará e instalará el resto paquetes necesitados por el proyecto para que este funcione correctamente una vez que este sea montado y ejecutado. 
La base de datos que utiliza el sistema también se ve 

#### Sin Docker

En el caso de que se quiera utilizar el proyecto sin utilizar Docker, es necesario:

1. -NodeJS v10.16.0 o superior.
2. -Base de datos MySQL 8.0


Luego de la instalación, descargue el proyecto y, en un terminal, accese a la carpeta del proyecto y ejecute: 

```
npm i
```

Esto descargará todos los paquetes necesarios para el funcionamiento del proyecto.

Luego de esto, cree una base de datos mySQL y use el script encontrado en *apicultoresrdd/dockerFileMysql/scripts*. Luego, cambie las credenciales encontradas en el documento src/keys.js por las credenciales de la base de datos que creó.

Finalmente, realice la query:

```
ALTER USER 'root' IDENTIFIED WITH mysql_native_password BY '123'
```

En la base de datos, cambiando 'root' por cualquier usuario con privilegios que actualmente exista en la base de datos.


### Instalación

Serie de pasos para poder ejecutar el proyecto

Clonar del repositorio http://gitlabtrans.face.ubiobio.cl:8081/tddfelipebenjamin/apicultoresrdd.git

```
git clone http://gitlabtrans.face.ubiobio.cl:8081/tddfelipebenjamin/apicultoresrdd.git
```
Ingresar al directorio del proyecto clonado

```
cd apicultoresrdd/                                                                                                    
```

Crear imagen node js de la aplicación

```
docker build -t tddopis .                                                                                               
```

Ingresar a directorio del Dockerfile mysql

```
cd dockerFileMysql/                                                                                           
```

Crear imagen para el servidor de la base de datos local mysql
