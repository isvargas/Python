#pyPortScan -  Exemplo de portscan utilzando Python
#Este exemplo didatico e serve unicamente para mostrar como trabalhar com parametros
#enviados pela linha de comando, criar funcoes e utilizar sockets TCP/IP.
import sys;
import socket;
 
#funcao principal, que realiza o scan
def scan(host, inicio, fim):
    #array que armazenara as portas abertas
    portas = []
 
    #loop principal
    for p in range(int(PORTA_INICIO), int(PORTA_FIM) + 1): #a funcao range(inicio, fim) retorna todos os valores entre dois numeros
        try:
            print '\rPorta:', p,
            #criamos o socket TCP
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
             
            #conectamos noss socket ao host e porta especificados
            tcp.connect((HOST,p))
             
            #se nao deu erro, conectou. Adiciono a porta ao array portas[]
            portas.append(p)
             
            #fecho a conexao
            tcp.close()
        except:
            #se deu erro ao abrir a conexao, passo adiante
            pass
 
    #ao concluir o loop, mostra o array com as portas encontradas
    print '\rScan concluido!'
    if len(portas) > 0:
        print 'Portas abertas:', portas
    else:
        print 'Nenhuma porta aberta :('
 
#verificamos se foram passados paramatros por linha de comand
if len(sys.argv) == 4:
    #se foram informados os parametros, repasso para variaveis formatando conforme o caso
    HOST         = sys.argv[1]
    PORTA_INICIO = sys.argv[2]
    PORTA_FIM    = sys.argv[3]
     
    #executo o scan
    scan(HOST, PORTA_INICIO, PORTA_FIM)
else:
    #se nao foram encontrados todos os parametros, mostro a sintaxe do programa
    print "----------------------------------------------------"
    print "pyPortScan - exemplo didatico de portscan com Python"
    print "----------------------------------------------------"
    print "\n\rSintaxe: python %s host porta_inicial porta_final" % sys.argv[0]
    print "\n\rExemplo: python %s 127.0.0.1 20 100" % sys.argv[0]
