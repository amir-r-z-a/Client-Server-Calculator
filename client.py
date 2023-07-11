import socket


def main():
    host = '127.0.0.1'
    port = 6000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # message you send to server
    while True:
        message = input("put yur operation here : ")
        s.send(message.encode('ascii'))
        data = s.recv(1024)
        print('server :', str(data.decode('ascii')))
        if message == "finished":
            break
        else:
            continue
    s.close()


if __name__ == '__main__':
    main()
