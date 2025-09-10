import socket

def start_server():
    host = socket.gethostbyname(socket.gethostname())
    PORT = 60000

    with open('index.html', 'r') as pag:
        homepage = pag.read()

    # # URL da imagem de redirecionamento 
    # redirect_image_url = f'https://www.storageja.com.br/assets/img/uploads/topologias-de-redes-9.webp'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, PORT))
    s.listen()
    
    print(f"Servidor ouvindo em {host}:{PORT}")

    try:
        running = True
        while running:
            conn, addr = s.accept()
            data = conn.recv(2000)

            dataP = data.split(b' ')

            if dataP[0] == b'GET':
                if dataP[1] == b'/':
                    resp = ('HTTP/1.1 200 OK\r\n' + 'Content-Type: text/html\r\n' + 'Content-Length: ' + str(len(homepage)) + '\r\n\r\n' + (homepage))
                    resp = str.encode(resp)
                    conn.sendall(resp)

                # else:
                #     # Redirecionamento para a URL da imagem
                #     resp = ('HTTP/1.1 301 Moved Permanently\r\n' + f'Location: {redirect_image_url}\r\n\r\n')
                #     conn.sendall(resp.encode())

            conn.close()

    except KeyboardInterrupt:
        print("\nConexão finalizada pelo usuário")
        running = False

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        s.close()
        print("Socket fechado")

if __name__ == "__main__":
    start_server()
