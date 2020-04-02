# App Vacunatorio

El proyecto presente en este repositorio corresponde a un mantenedor de registros de vacunas a pacientes 

### Instalación

Serie de pasos para poder desplegar la App

Clonar del repositorio https://github.com/opazoFelipe/ProyectoFinalPython

```
git clone https://github.com/opazoFelipe/ProyectoFinalPython
```
Ingresar al directorio del proyecto clonado

```
cd ProyectoFinalPython/                                                                                                
```

Instalar dependencias

```
pip install -r requirements.txt                                                                                            
```

Copiar todo el contenido del archivo script.db y ejecutarlo en una terminal MYSQL o en un Gestor de Bases de datos compatible

Es necesario asignar credenciales especificas de la configuracion de su servidor MYSQL instalado. 
Para hacerlo, ingrese al archivo App.py, en el apartado "# Configurar conexion a base de datos" y asigne las credenciales correspondientes.

Desplegar la Aplicacion

```
python App.py                                                                                         
```

Acceder a la App desde un navegador usando la URL

```
localhost:3000                                                                                      
```
