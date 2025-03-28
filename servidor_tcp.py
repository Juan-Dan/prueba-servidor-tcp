import socket

host = "127.0.0.1" #host local
puerto = 5000 #puerto del servidor

def inicar_servidor():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as servidor_socket:
        servidor_socket.bind((host,puerto))
        servidor_socket.listen()
        print(f"Servidor escuchando en {host}:{puerto}")

        while True:
            cliente_socket, cliente_direccion = servidor_socket.accept()
            with cliente_socket:
                print(f"Conexión establecida con {cliente_direccion}")

                while True: 
                    datos = cliente_socket.recv(1024).decode()
                    if not datos:
                        break
                    print("Mensaje recibido: {datos}")
                    if datos.upper() == "DESCONEXION":
                        print(f"Cliente {cliente_direccion} desconectado")
                        break
                    respuesta = datos.upper()
                    cliente_socket.sendall(respuesta.encode())

if __name__ == "__main__":
    inicar_servidor
             