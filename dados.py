import psycopg2
import pandas as pd

try:
    conn = psycopg2.connect(user = "postgres",
                                password = "root",
                                host = "localhost",
                                port = "5432",
                                database = "postgres")
    print("BD Conectado!")
    cur = conn.cursor()
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
    print("Falha conexao com o banco!")

finally:

   #select=('select primeira_dez, segunda_dez, terceira_dez, quarta_dez, quinta_dez, sexta_dez from megasena')
   select_d1=('select primeira_dez from megasena')
   select_d2=('select segunda_dez from megasena')
   select_d3=('select terceira_dez from megasena')
   select_d4=('select quarta_dez from megasena')
   select_d5=('select quinta_dez from megasena')
   select_d6=('select sexta_dez from megasena')
   #select=[, select_d2,select_d3, select_d4, select_d5, select_d6]

   #select=('select * from megasena')

   
   
   cur.execute(select_d1)
   dezenas1=cur.fetchall()
   cur.execute(select_d2)
   dezenas2=cur.fetchall()
   cur.execute(select_d3)  
   dezenas3=cur.fetchall()
   cur.execute(select_d4)  
   dezenas4=cur.fetchall()
   cur.execute(select_d5)  
   dezenas5=cur.fetchall()
   cur.execute(select_d6)  
   dezenas6=cur.fetchall()
   

   dezenas=(dezenas1, dezenas2, dezenas3, dezenas4, dezenas5, dezenas6)

   #print(dezenas)
   df= pd.DataFrame(dezenas)  #columns = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6']

   print(df)
