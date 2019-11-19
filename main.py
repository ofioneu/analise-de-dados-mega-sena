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
 
    @app.route('/', methods = ['POST', 'GET'])
    def analise():
        dezenas_a=[]
        dezenas_b=[]
        for dezenas in range(60):
            cur.execute('select count(*) from megasena  where primeira_dez='+ str(dezenas))
            a=cur.fetchone()
            cur.execute('select count(*) from megasena  where sexta_dez='+ str(dezenas))
            b=cur.fetchone()
            dezenas_a.append(a)
            dezenas_b.append(b)
            
        print('lista de dezenas A: ', dezenas_a)
        print('lista de dezenas B: ', dezenas_b)
        dezenas_a_int=[]
        for e in dezenas_a:
            dezenas_a_int.append(int(e))
        

        @socketio.on('message')
        def menssagem(message):
            print(message) 
            emit('message', dezenas_a_int)
            time.sleep(1)
        return render_template('home.html')

if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', port= 5000)