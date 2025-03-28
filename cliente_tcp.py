import socket

host = "127.0.0.1"
puerto = 5000

def iniciar_cliente():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as cliente_socket: 
        cliente_socket.connect((host,puerto))
        print(f"Conectado al servidor {host}:{puerto}")

        while True: 
            mensaje = input("Escribre un mensaje: ")
            cliente_socket.sendall(mensaje.encode())

            if mensaje.upper() == "DESCONEXION":
                print("Desconectado del servidor")
                break

            respuesta = cliente_socket.recv(1024).decode()
            print(f"Respuesta del servidor: {respuesta}")

if __name__ == "__main__":
    iniciar_cliente()