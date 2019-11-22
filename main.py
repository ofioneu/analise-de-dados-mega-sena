from flask import Flask
from flask import render_template
import json
from flask_socketio import SocketIO
from flask_socketio import send, emit
import time
import psycopg2
 
app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = '@11tahe89!'
socketio = SocketIO(app)


try:
    conn = psycopg2.connect(user = "postgres",
                                password = "root",
                                host = "35.239.106.233",
                                port = "5433",
                                database = "postgres")
    print("BD Conectado!")
    cur = conn.cursor()
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
    print("Falha conexao com o banco!")

finally:
 
    @app.route('/')
    def analise():
        dezenas_a=[]
        dezenas_b=[]
        dezenas_c=[]
        dezenas_d=[]
        dezenas_e=[]
        dezenas_f=[]
        for dezenas in range(61):
            cur.execute('select count(*) from megasena  where primeira_dez='+ str(dezenas))
            a=cur.fetchone()
            dezenas_a.append(a)
        for dezenas2 in range (61):
            cur.execute('select count(*) from megasena  where segunda_dez='+ str(dezenas2))
            b=cur.fetchone()
            dezenas_b.append(b)
        for dezenas3 in  range(61):
            cur.execute('select count(*) from megasena  where terceira_dez='+ str(dezenas3))
            c=cur.fetchone()
            dezenas_c.append(c)
        for dezenas4 in  range(61):
            cur.execute('select count(*) from megasena  where quarta_dez='+ str(dezenas4))
            d=cur.fetchone()
            dezenas_d.append(d)
        for dezenas5 in  range(61):
            cur.execute('select count(*) from megasena  where quinta_dez='+ str(dezenas5))
            e=cur.fetchone()
            dezenas_e.append(e)
        for dezenas6 in  range(61):
            cur.execute('select count(*) from megasena  where sexta_dez='+ str(dezenas6))
            f=cur.fetchone()
            dezenas_f.append(f)
        
                        
        dezenas_a_str=[]
        dezenas_b_str=[]
        dezenas_c_str=[]
        dezenas_d_str=[]
        dezenas_e_str=[]
        dezenas_f_str=[]

        dezenas_a_int=[]
        dezenas_b_int=[]
        dezenas_c_int=[]
        dezenas_d_int=[]
        dezenas_e_int=[]
        dezenas_f_int=[]
        
        for a1 in dezenas_a:
            dezenas_a_str.append(str(a1).replace('(', '').replace(',)', ''))
        
        for a2 in dezenas_a_str:
            dezenas_a_int.append(int(a2))

        for b1 in dezenas_b:
            dezenas_b_str.append(str(b1).replace('(', '').replace(',)', ''))
        
        for b2 in dezenas_b_str:
            dezenas_b_int.append(int(b2))
        
        for c1 in dezenas_c:
            dezenas_c_str.append(str(c1).replace('(', '').replace(',)', ''))
        
        for c2 in dezenas_c_str:
            dezenas_c_int.append(int(c2))
        for d1 in dezenas_d:
            dezenas_d_str.append(str(d1).replace('(', '').replace(',)', ''))
        
        for d2 in dezenas_d_str:
            dezenas_d_int.append(int(d2))
        
        for e1 in dezenas_e:
            dezenas_e_str.append(str(e1).replace('(', '').replace(',)', ''))
        
        for e2 in dezenas_e_str:
            dezenas_e_int.append(int(e2))
        for f1 in dezenas_f:
            dezenas_f_str.append(str(f1).replace('(', '').replace(',)', ''))
        
        for f2 in dezenas_f_str:
            dezenas_f_int.append(int(f2))

        um_com_dois=[]
        tres_com_quatro=[]
        cinco_com_seis=[]
        soma1=[]
        soma_final=[]
        for indice in range(61):
            um_com_dois.append(dezenas_a_int[indice] + dezenas_b_int[indice])

        for indice1 in range(61):
            tres_com_quatro.append(dezenas_c_int[indice1] + dezenas_d_int[indice1])
        
        for indice2 in range(61):
            cinco_com_seis.append(dezenas_e_int[indice2] + dezenas_f_int[indice2])
        
        for indice3 in range(61):
            soma1.append(um_com_dois[indice3] + tres_com_quatro[indice3])
        
        for indice4 in range(61):
            soma_final.append(soma1[indice4] + cinco_com_seis[indice4])
        
                
        
                
        print('Soma final : ', soma_final)
        
        dezenas_dict = {
            "soma": soma_final,
            "d1": dezenas_a_int,
            "d2": dezenas_b_int,
            "d3": dezenas_c_int,
            "d4": dezenas_d_int,
            "d5": dezenas_e_int,
            "d6": dezenas_f_int,
            }

        dezenas_json = json.dumps(dezenas_dict)
        

        @socketio.on('message')
        def menssagem(message):
            print(message) 
            emit('message', dezenas_json)
            time.sleep(1)
        return render_template('home.html')

if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', port= 5000)