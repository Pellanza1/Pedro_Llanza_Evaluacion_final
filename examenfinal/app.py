from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal con botones
@app.route('/')
def index():
    return render_template('index.html')

# Ejercicio 1: Compra de pinturas
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])

        precio_por_tarro = 9000
        total_sin_descuento = tarros * precio_por_tarro

        descuento = 0
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        total_con_descuento = total_sin_descuento * (1 - descuento)

        return render_template(
            'ejercicio1.html',
            nombre=nombre,
            edad=edad,
            total_sin_descuento=total_sin_descuento,
            total_con_descuento=total_con_descuento,
            descuento=int(descuento * 100)
        )

    return render_template('ejercicio1.html')

# Ejercicio 2: Inicio de sesión
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    usuarios = {'juan': 'admin', 'pepe': 'user'}
    mensaje = None

    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']

        if usuario in usuarios and usuarios[usuario] == password:
            if usuario == 'juan':
                mensaje = f"Bienvenido administrador {usuario}"
            elif usuario == 'pepe':
                mensaje = f"Bienvenido usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
