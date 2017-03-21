#importar classe sqlite3
import sqlite3;
 
#criando um db no sistema de arquivos
conexao = sqlite3.connect('banco.db');
 
#criando cursor
cursor = conexao.cursor();
 
#campo id
ID = 0;
 
#criar tabela
def criar_tabela():
    try:
        sql = 'CREATE TABLE PESSOA(id INTEGER, NOME VARCHAR, ENDERECO VARCHAR)';
        cursor.execute(sql);
        print "Tabela criada.";
    except:
        pass; #print "Tabela jah existe."; #o pass nao faz nada, eh usado quando a sintaxe exige um comando mas a semantica do programa nao requer nenhuma acao.
 
#add dados
def add_pessoa(id_pessoa, nome, endereco):
    sql = 'INSERT INTO PESSOA(id,NOME,ENDERECO) VALUES(?,?,?)';
    cursor.execute(sql,(id_pessoa,nome,endereco));
    conexao.commit();
    print "Pessoa registrada.";
 
#listar pessoas
def lista_pessoas():
    sql = "SELECT * FROM PESSOA";
    cursor.execute(sql);
    result = cursor.fetchall();
    for pessoa in result:
        print "Id:", pessoa[0];
        print "Nome:", pessoa[1];
        print "Endereco:", pessoa[2];
 
#menu do sistema
criar_tabela();
opcao = 0;
while opcao != 3:
    print "=================================="
    print "PROGRAMA EXEMPLO DE BANCO DE DADOS"
    print "=================================="
    print "[1]  Cadastrar Pessoa";
    print "[2]  Listar Pessoas";
    print "[3]  Sair";
 
    opcao = input("Opcao:");
 
    if opcao == 1:
        ID += 1;
        nome = raw_input("Nome:");
        endereco = raw_input("Endereco:");
        add_pessoa(ID,nome,endereco);
    elif opcao == 2:
        lista_pessoas();
    elif opcao == 3:
        print "Ateh mais ;)";
    else:
        print "Opcao invalida.";
 
print 'Concluido.';
