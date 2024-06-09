# Proyecto - Message Broker
  Proyecto para el curso de Sistemas Operativos, de la Universidad Nacional de Costa Rica (durante el primer ciclo de 2024). Realizado por los estudiantes:
  - Jose Pablo Miranda Muñoz
  - Saúl Araya Salas
  - Alexander Gutiérez Ugalde
## Instrucciones de uso
  1. Descargar e instalar GNUWIN32 y Chocolatey
  2. Al instalar los componentes anteriores. Se debe abrir el proyecto con el editor de código Visual Studio Code, y abriendo una terminal, se ejecutan los siguientes comandos:
      - **'make modules'**: Para instalar los modulos necesarios para el correcto funcionamiento del proyecto.
      - **'make compile-grpc-py', 'make run-server-py' y 'make run-client-py'**: En caso de tener instalado Python en el equipo, se ejecutan los comandos anteriores. Se encargan de compilar el archivo broker.proto para actualizar los archivos autogenerados por proto. Y los dos siguientes se encargan de inicializar el servidor y los clientes.
      - **'make compile-grpc-py3', 'make run-server-py3' y 'make run-client-py3'**: En caso de tener instalado Python3 en el equipo, hace lo mismo que los comandos anteriores.
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
