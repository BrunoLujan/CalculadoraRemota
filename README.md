# CalculadoraRemota
Ejercicio calculadora remota con Apache Thrift y RPC
 
 1. Posicionate en la carpeta principal de la carpeta; donde se encuentra 'docker-compose.yml'
 2. Ejecutar el comando: docker-compose build
 3. Ejecutar el comando: docker-compose create
 4. Visualizar los nombres de los contenedores creado: docker-compose ps -a
 5. Iniciar el contenedor del servidor con: dockerc-start [nombreContenedorServidor]
 6. Iniciar el contenedor del cliente con: docker start -i [nombreContenedorServidor]
