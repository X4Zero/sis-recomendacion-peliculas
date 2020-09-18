from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
from recursos import *
import time
import threading
app = Flask(__name__)

df=''
cosine_sim=''
indices=''
def espera():
    print("Esperando...")
    global CC
    while True:
        if cosine_sim=='':
            time.sleep(5)
        else:
            break

def iniciar():
    global df
    global cosine_sim
    global indices
    df,indices,cosine_sim = cargar_variables()
    print(df.shape)
    print(cosine_sim.shape)
    print(indices.shape)

@app.before_first_request
def activate_job():
    thread = threading.Thread(target=iniciar)
    thread.start()


@app.route('/')
def index():
    global df
    global cosine_sim
    global indices
    print("**********INDEX**********")
    espera()
    # df,indices,cosine_sim = cargar_variables()

    return render_template('index.html')

@app.route('/busqueda', methods=['POST'])
def busqueda():
    global df
    global cosine_sim
    global indices
    print("**********BUSQUEDA**********")
    espera()
    if request.method == 'POST':
        titulo = request.form['titulo']
    
    print("titulo: ",titulo)

    resultado = ObtenerPeliculaCoincidencia(titulo,df)

    print(resultado)
    data = list(zip(resultado.index,resultado.values))
    return render_template('index.html', data = data)

@app.route('/recomendar/<id>')
def recomendar(id):
    global df
    global cosine_sim
    global indices
    print("**********RECOMENDAR**********")
    espera()
    print("id: ",id)

    recomendaciones = ObtenerRecomendacion(int(id),df,cosine_sim,indices)
    peli=df.loc[int(id),'title']
    print(recomendaciones)
    data = list(zip(recomendaciones.index,recomendaciones.values))
    return render_template('index.html', recomendaciones = data,peli=peli)

if __name__ == '__main__':
    app.run(port=4000, debug=True)