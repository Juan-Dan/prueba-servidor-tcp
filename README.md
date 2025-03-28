# prueba-servidor-tcp
Aqui podran examinar mis archivos creados para la prueba empresarial
# Servidor y Cliente TCP en Python

Este proyecto implementa un servidor y un cliente TCP en Python que pueden comunicarse en localhost usando el puerto 5000.

## 🔧 Ejecución

### **Ejecutar el servidor**
python servidor_tcp.py

El servidor escuchará en 127.0.0.1:5000 y estará listo para aceptar conexiones.

### **Ejecutar el cliente**
En otra terminal, ejecuta:
python cliente_tcp.py

El cliente se conectará al servidor y permitirá enviar mensajes.

## Pruebas Manuales

### **Caso 1: Mensaje normal**
1. Escribe un mensaje en el cliente (por ejemplo, "hola").
2. El servidor responderá con el mensaje en mayúsculas ("HOLA").

### **Caso 2: Desconexión**
1. En el cliente, escribe "DESCONEXION".
2. El servidor cerrará la conexión con ese cliente.
3. El cliente se cerrará automáticamente.

---
