# Proyecto - Message Broker
  Proyecto para el curso de Sistemas Operativos, de la Universidad Nacional de Costa Rica (durante el primer ciclo de 2024). Realizado por los estudiantes:
  - Jose Pablo Miranda Muñoz
  - Saúl Araya Salas
  - Alexander Gutiérez Ugalde
## Instrucciones de uso
  1. Descargar e instalar GNUWIN32 y Chocolatey
  2. Al instalar los componentes anteriores. Se debe abrir el proyecto con el editor de código Visual Studio Code, y abriendo una terminal, se ejecutan los siguientes comandos:
      - **'make modules'**: Para instalar los modulos necesarios para el correcto funcionamiento del proyecto.
      - **'compile-grpc-python, compile-grpc-python3'**: Para compilar el archivo del broker.proto el cual crea las clases necesarias para implementar el servicio y los procedimientos remotos y el servidor empleados para este proyecto.
      - **'Para inicializar el servidor'**: Para inicializar el servidor se debe de ingresar a la carpeta build y ejecutar el comando python servidor.py, o bien, python3 servidor.py
      - **'Para instanciar un cliente'**: Para instanciar un cliente se debe de ingresar a la carpeta build y ejecutar el comando python cliente.py, o bien, python3 cliente.py
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
