import socket

# 创建一个服务器socket，绑定到本地IP和端口
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8080))
server_socket.listen()

print('Server is running on http://127.0.0.1:8080')

while True:
    # 等待客户端连接
    client_socket, client_address = server_socket.accept()
    print('New client connected:', client_address)

    # 接收客户端发送的请求
    request = client_socket.recv(1024)
    print('Received request:', request)

    # 构造响应内容，这里只返回一个简单的Hello World!
    response = b'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n<html><body><h1>Hello World!</h1></body></html>'

    # 发送响应内容给客户端
    client_socket.sendall(response)

    # 关闭客户端socket
    client_socket.close()
