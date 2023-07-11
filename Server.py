import socket
import math
from timeit import default_timer as timer
from _thread import *
import threading

print_lock = threading.Lock()


def threaded(c):
    while True:
        data = c.recv(1024)
        data2 = str(data.decode('ascii'))
        if data2 == "finished":
            data2 = "by by"
            c.send(data2.encode('ascii'))
            # lock released on exit
            print_lock.release()
            break

        if not data2[0] == "$":
            wrong = "wrong"
            c.send(wrong.encode('ascii'))
            continue
        new_data = data2.split("$")
        print(new_data)
        operator = new_data[1]
        op1 = int(new_data[2])
        if len(new_data) > 4:
            op2 = int(new_data[3])
        delta = 0
        res = 0
        if operator == " Add ":
            start = timer()
            res = op1 + op2
            end = timer()
            delta = end - start
        elif operator == " Subtract ":
            start = timer()
            res = op1 - op2
            end = timer()
            delta = end - start
        elif operator == " Divide ":
            start = timer()
            res = op1 / op2
            end = timer()
            delta = end - start
        elif operator == " Multiply ":
            start = timer()
            res = op1 * op2
            end = timer()
            delta = end - start
        elif operator == " Sin ":
            start = timer()
            res = math.sin(op1)
            end = timer()
            delta = end - start
        elif operator == " Cos ":
            start = timer()
            res = math.cos(op1)
            end = timer()
            delta = end - start
        elif operator == " Tan ":
            start = timer()
            res = math.tan(op1)
            end = timer()
            delta = end - start
        elif operator == " Cot ":
            start = timer()
            res = 1 / (math.tan(op1))
            end = timer()
            delta = end - start
        else:
            wrong = "wrong"
            c.send(wrong.encode('ascii'))
            continue
        c.send((str(delta) + " $ " + str(res)).encode('ascii'))
    c.close()


def main():
    host = ""

    port = 6000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    s.listen(5)
    print(f"socket on port : {port} ")

    print("--listening--")

    while True:
        c, addr = s.accept()
        print(f'connection from port {addr[1]}')
        print_lock.acquire()

        start_new_thread(threaded, (c,))
    s.close()


if __name__ == '__main__':
    main()
