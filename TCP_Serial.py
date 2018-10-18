#Controlar Serial por TCP/IP
#
#Neste exemplo criamos um servidor que recebe comandos pela rede
#e, com base neste comando, envia uma mensagem para a porta Serial.
#
#Como isso podemos controlar dispositos com o Arduino, por exemplo, 
#pela Internet.
#
#Descricao: Se o cliente digitar 1 enviamos "L" (ligar) para a Serial,
#se digitar 2 enviamos "D" (desligar) para a Serial.
#
#Ivan S. Vargas - contato@is5.com.br
#
import socket;
import string;
import serial;

HOST = '192.168.2.1';
PORT = 5000;

comport = serial.Serial("COM5", 9600);

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
tcp.bind((HOST, PORT));
tcp.listen(1);

print 'Escutando...';
while True:
    con, cliente = tcp.accept();
    print 'Conectado por', cliente;
    while True:
        msg = con.recv(1024)
	 if (string.find(msg, "1") >=0):
            print "Ligando...";
            comport.write("L");
        if (string.find(msg, "2") >= 0):
            print "desligando...";	
            comport.write("D");
        if not msg: break;
    print 'Finalizando conexao do cliente', cliente;
    con.close();
