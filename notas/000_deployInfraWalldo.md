## Deploy Infra Wall-do
### Dependencias
- [Instalar Docker](https://docs.docker.com/install/)
- [Instalar docker-compose](https://docs.docker.com/compose/install/#install-compose)
- Clonar repo

### Despliegue






### Info

### walldo_py
- Contenedor con python + SSH
- Es donde se ejecuta Walldo y desde donde se lanzaran los comandos via SSH al resto de hosts.


### MongoDB
- 'mongo' es la bbdd y 'mongo-express' una interfaz gráfica:
  - Volumen para datos persistentes
  
### ELK
- Fork del repo [docker-ELK](https://github.com/deviantony/docker-elk)
- De momento no usamos logstash, por lo que esta comentado en el compose.s