#importamos a lib de acesso
import kinterbasdb; #instalar o driver - download firebirdsql.org
 
#conectamos ao banco de dados
con = kinterbasdb.connect(dsn='localhost:c:/meubanco.fdb',user='sysdba',password='masterkey');
 
#buscamos o cursor
cursor = con.cursor();
 
#select para listar o nome de todos os clientes cadastrados
sql = 'SELECT NOME FROM CLIENTES ORDER BY NOME';
 
#executamos o select
cursor.execute(sql);
 
#percorremos todos os registros mostrando o nome retornado
for pessoa in cursor.fetchall():
    print pessoa[0]; 
    #o índice aqui refere-se ao campo retornado. Como somente retornamos o nome existe apenas um campo retornado. O índice começa em zero.
    #se o select retornasse mais dados, como NOME, ENDERECO, TELEFONE, por exemplo, o endereco seria pessoa[1] e o telefone pessoa[2]
 
#depois de retornarmos os dados, fechamos a conexão
con.close();
