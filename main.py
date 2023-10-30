import socket
import urls
import setup

HOST = '0.0.0.0'
PORT = setup.PORT


def handle_client(client_socket):
    request_data = client_socket.recv(1024)
    if not request_data:
        return

    # Parse the request data to extract the HTTP method
    request_lines = request_data.decode('utf-8').split('\n')
    first_line = request_lines[0].strip()
    http_method = first_line.split(' ')[0]
    path = first_line.split(' ')[1]

    # Print the HTTP method and request received from the client
    print(f"HTTP Method: {http_method}")
    requestdata = request_data.decode('utf-8')  # TODO: Evaluate necessity
    print(requestdata)

    content = urls.GB(path)  # TODO: Get from urls TODO: custom heads?

    head = b"HTTP/1.1 200 OK\r\nContent-Length: " + str(len(content)).encode('utf-8')

    body = b"\r\n\r\n" + content  # TODO: get response from variable TODO: confirm head/body split is correct

    if http_method == "GET":  # TODO: add support for other HTTP methods
        client_socket.send(head + body)
    elif http_method == "HEAD":
        client_socket.send(head)
    else:
        client_socket.send(b"HTTP method not recognized")
    client_socket.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"Listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")
        handle_client(client_socket)


if __name__ == "__main__":
    main()
