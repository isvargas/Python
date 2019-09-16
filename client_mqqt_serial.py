# CONECTAR A UM BROKER MQTT COM USUARIO E SENHA
# ENVIAR COMANDO PARA PORTA SERIAL DE ACORDO
# COM A MENSAGEM RECEBIDA
# ---------------------------------------------
# instalar o paho-mqtt:
# python -m pip  install paho-mqtt
#
# instalar serial
# python -m pip install pyserial
#
# I.S.V
import paho.mqtt.client as mqtt #import the client
import time
import serial

SERVIDOR = "soldier.cloudmqtt.com"
PORTA    = 13919 
USUARIO  = "nmrbnrst"
SENHA    = "F8OUh79L_T07"
TOPICO   = "casa/quarto"

PORTA_COM = "COM5"
BAUD_RATE = 115200

def escrever_porta(str_cmd):
   try:
       cmd = str.encode(str_cmd);
       print('Escrevendo na porta',str_cmd);
       porta = serial.Serial(PORTA_COM, BAUD_RATE)
       porta.write(str_cmd)
       time.sleep(5)
       porta.close()
       
       print('[+] Mensagem enviada para a porta')
   except:
       #serial.SerialException:
       print("[!] ERRO: Verifique se ha algum dispositivo conectado na porta!")


def ligar():
    escrever_porta('L')

def desligar():
    escrever_porta('D')

def exec_cmd(cmd):
    try:
        if '#LIGAR#' in cmd:
            ligar()
            return 1
        
        if '#DESLIGAR#' in cmd:
            desligar()
            return 1
    except:
        print('[!] Erro ao executar comando',cmd)


def on_message(client, userdata, message):
    strcmd = str(message.payload.decode("utf-8"))
    print("Mensagem recebida:",strcmd)
    exec_cmd(strcmd)

def connect_broker():
    try:        
        print("[+] Criando instancia Client")
        client = mqtt.Client("P1")     #create new instance
        #se for utilizar websockets:
        #client = mqtt.Client("teste",transport='websockets')
        client.on_message=on_message   #attach function to callback

        print("[+] Conectando ao broker MQTT", SERVIDOR)
        client.username_pw_set(username=USUARIO,password=SENHA)
        client.connect(SERVIDOR,PORTA)  #connect to broker
        client.loop_start()             #start the loop

        print("[+] Assinando topico",TOPICO)
        client.subscribe(TOPICO)

        print("[+] Publicando mensagen no topico",TOPICO)
        client.publish(TOPICO,"HELLO")

        #time.sleep(4)      #wait
        #client.loop_stop() #stop the loop
    except:
        print('[!] Eita, deu erro!!!')
        return 0

connect_broker()


