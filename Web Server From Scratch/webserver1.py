import socket
HOST, PORT = '', 8888
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Đoạn mã này tạo một socket TCP thông qua giao thức AF_INET (IPv4)
# và giao thức truyền thông SOCK_STREAM (TCP)
#  Sau đó, nó thiết lập một tuỳ chỉnh socket để cho phép sử dụng lại 
# địa chỉ và cổng sau khi socket đã được sử dụng. Cuối cùng, nó ràng buộc (bind) socket đó đến 
# một địa chỉ IP và cổng cụ thể và sau đó lắng nghe kết nối đến socket đó.

# Allow to reuse the same address
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

"""
(HOST, PORT) là một tuple chứa địa chỉ IP (HOST) và 
số cổng (PORT) mà bạn muốn socket lắng nghe. 
Ví dụ: (127.0.0.1, 8080) sẽ liên kết socket để lắng nghe trên
địa chỉ IP localhost (127.0.0.1) và cổng 8080.
"""
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print(f"Serving on {PORT}")
print(listen_socket.getsockname()[:2])
while True:
    client_connection, client_address = listen_socket.accept()
    request_data = client_connection.recv(1024)
    print(request_data.decode('utf-8'))

    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)
    client_connection.close()
