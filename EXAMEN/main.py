from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/pinturas', methods=['GET', 'POST'])
def pinturas():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        tarros = request.form['tarros']

        valor_sin_desc = int(tarros)*9000
        if int(edad)>=18 and int(edad)<=30:
            desc = valor_sin_desc * 0.15
        elif int(edad)>30:
            desc = valor_sin_desc * 0.25
        else:
            desc = 0
        pago = valor_sin_desc - desc

        return render_template('pinturas.html',
                               show_results=True,
                               nombre_cliente=nombre,
                               sin_descuento=valor_sin_desc,
                               descuento=desc,
                               total_pago=pago)

    return render_template('pinturas.html')



@app.route('/sesion', methods=['GET', 'POST'])
def sesion():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasena = request.form['contraseña']

        if nombre == 'juan' and contrasena == 'admin':
            mensaje = 'Bienvenido Administrador juan'
        elif nombre == 'pepe' and contrasena == 'user':
            mensaje = 'Bienvenido Usuario pepe'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

        return render_template('sesion.html',
                               show_results=True,
                               mensaje=mensaje)

    return render_template('sesion.html')

if __name__ == '__main__':
    app.run(debug=True)