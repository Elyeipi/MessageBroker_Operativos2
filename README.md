# Proyecto - Message Broker
  Proyecto para el curso de Sistemas Operativos, de la Universidad Nacional de Costa Rica (durante el primer ciclo de 2024). Realizado por los estudiantes:
  - Jose Pablo Miranda Muñoz
  - Saúl Araya Salas
  - Alexander Gutiérez Ugalde
## Instrucciones de uso
  1. Descargar e instalar GNUWIN32 y Chocolatey, esto para instalar las funcionalidades del comando make (para manejar Makefiles). Al ejecutar el comando **'choco install make'** a través de una PowerShell con permisos de administrador.
  2. Al instalar los componentes anteriores. Se debe abrir el proyecto con el editor de código Visual Studio Code, y haciendo uso de una terminal integrada, se ejecutan los siguientes comandos:
      - **'make modules'**: En la carpeta raíz del proyecto, se ejecuta este comando para instalar los módulos necesarios para el funcionamiento del proyecto. Actualiza primeramente el instalador de paquetes de Python (PIP), para posteriormente instalar módulos respectivos.
      - **'compile-grpc-python' y compile-grpc-python3'**: Para compilar el archivo del broker.proto, el cual se encarga de crear las clases necesarias para implementar los servicios, los procedimientos remotos y el servidor.
    
### Ejecución de los programas
  - **Para inicializar el servidor**: Se debe de ingresar a la carpeta build y ejecutar el comando python servidor.py, o bien, python3 servidor.py. Dependerá de los paquetes de Python que se encuentren en el equipo.
  - **'Para instanciar un cliente'**: Se debe de ingresar a la carpeta build y ejecutar el comando python cliente.py, o bien, python3 cliente.py. Dependerá de los paquetes de Python que se encuentren en el equipo.
## Recursos consultados
  + https://gnuwin32.sourceforge.net/packages/make.htm
  + https://chocolatey.org/install
  + https://grpc.io/docs/languages/python/basics/
  + https://grpc.io/docs/languages/python/
  + https://protobuf.dev/overview/
  + https://www.youtube.com/watch?v=0sVGnxg6Z3k&list=PLfqABt5AS4FmuQf70psXrsMLEDQXNkLq2&index=11
  + https://www.geeksforgeeks.org/multithreading-python-set-1/
  + https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/
  + https://stackoverflow.com/questions/54942240/how-to-design-publish-subscribe-pattern-properly-in-grpc
  + https://stackoverflow.com/questions/47831895/how-do-i-handle-streaming-messages-with-python-grpc
  + https://stackoverflow.com/questions/63177939/broadcasting-message-from-grpc-server-to-all-some-connected-clients-in-python
  + https://medium.com/@maryanngitonga/server-client-communication-using-grpc-with-a-real-life-example-267a0bcba1a9
