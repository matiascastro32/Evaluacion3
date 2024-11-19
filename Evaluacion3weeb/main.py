from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        # Recoge las notas y asistencia del formulario
        notas = [float(request.form[f'nota{i}']) for i in range(1, 4)]
        asistencia = float(request.form['asistencia'])
        promedio = sum(notas) / 3
        estado = 'Reprobado' if promedio <= 40 and asistencia <= 75 else 'Aprobado'
        resultado = {'promedio': promedio, 'estado': estado}
    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    if request.method == 'POST':
        # Recoge los nombres del formulario
        nombres = [request.form[f'nombre{i}'] for i in range(1, 4)]
        nombre_mas_largo = max(nombres, key=len)
        resultado = {'nombre': nombre_mas_largo, 'longitud': len(nombre_mas_largo)}
    return render_template('ejercicio2.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)


