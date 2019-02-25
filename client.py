from __future__ import print_function
import socket
# from contextlib import closing
import sys
import termios


def main():

    fd = sys.stdin.fileno()

    # fdの端末属性をゲットする
    # oldとnewには同じものが入る。
    # newに変更を加えて、適応する
    # oldは、後で元に戻すため
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)

    # new[3]はlflags
    # ICANON(カノニカルモードのフラグ)を外す
    new[3] &= ~termios.ICANON
    # ECHO(入力された文字を表示するか否かのフラグ)を外す
    new[3] &= ~termios.ECHO

    host = '127.0.0.1'
    port = 4000
    # bufsize = 4096

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    while True:
        try:
            # 書き換えたnewをfdに適応する
            termios.tcsetattr(fd, termios.TCSANOW, new)
            # キーボードから入力を受ける。
            # lfalgsが書き換えられているので、エンターを押さなくても次に進む。echoもしない
            ch = sys.stdin.read(1)

        finally:
            # fdの属性を元に戻す
            # 具体的にはICANONとECHOが元に戻る
            termios.tcsetattr(fd, termios.TCSANOW, old)

        print(ch, end='', flush=True)
        ch = ch.encode("utf-8")
        sock.send(ch)
        if ch == b"q":
            break


if __name__ == '__main__':
    main()
