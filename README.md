# App Vacunatorio

El proyecto presente en este repositorio corresponde a un mantenedor de registros de vacunas a pacientes 

### Instalación

Serie de pasos para poder desplegar la App

Clonar del repositorio https://github.com/opazoFelipe/ProyectoFinalPython con el comando:

```
git clone https://github.com/opazoFelipe/ProyectoFinalPython
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
