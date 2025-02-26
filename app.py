import os
from marlon import Marlon
from enzoc import Enzoc
from enzot import Enzot
from joaoBrugnolo import JoaoBrugnolo
from nicolas import Nicolas

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

@app.route('/marlon', methods=['GET'])
def marlon():    
    try:
        marlon = Marlon()
        valor = marlon.hipotenusa(40,20) 
        return render_template('valor.html', valor = valor)
    except Exception as e:
        return render_template('valor.html', valor = str(e))

@app.route('/enzoc', methods=['GET'])
def enzoc():    
    try:
        enzoc = Enzoc()
        valor = enzoc.hipotenusa(40,20) 
        return render_template('valor.html', valor = valor)
    except Exception as e:
        return render_template('valor.html', valor = str(e))

@app.route('/enzot', methods=['GET'])
def enzot():    
    try:
        enzot = Enzot()
    
        #valor = enzot.hipotenusa(40,20) 
        #return render_template('valor.html', valor = valor)
    
        valor = enzot.raizes(2,3,-5) 
        return render_template('valor.html', valor = valor)
    
    
    except Exception as e:
        return render_template('valor.html', valor = str(e))

@app.route('/joaoBrugnolo', methods=['GET'])
def joaoBrugnolo():    
    try:
        joaoBrugnolo = JoaoBrugnolo()
        valor = joaoBrugnolo.hipotenusa(40,20) 
        return render_template('valor.html', valor = valor)
    except Exception as e:
        return render_template('valor.html', valor = str(e))

@app.route('/nicolas', methods=['GET'])
def nicolas():    
    try:
        nicolas = Nicolas()
        valor = nicolas.hipotenusa(40,20) 
        return render_template('valor.html', valor = valor)
    except Exception as e:
        return render_template('valor.html', valor = str(e))


if __name__ == '__main__':
   app.run()
