from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal con el menú de formularios
@app.route('/')
def index():
    return render_template('base.html')

# Formulario de inscripción en curso
@app.route('/inscripcion', methods=['GET', 'POST'])
def inscripcion():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellidos = request.form.get('apellidos')
        curso = request.form.get('curso')
        return f"Nombre: {nombre}, Apellidos: {apellidos}, Curso: {curso}"
    return render_template('inscripcion.html')

# Formulario de registro de usuarios
@app.route('/usuarios', methods=['GET', 'POST'])
def usuarios():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellidos = request.form.get('apellidos')
        correo = request.form.get('correo')
        contrasena = request.form.get('contrasena')
        return f"Nombre: {nombre}, Apellidos: {apellidos}, Correo: {correo}, Contraseña: {contrasena}"
    return render_template('usuarios.html')

# Formulario de registro de productos
@app.route('/productos', methods=['GET', 'POST'])
def productos():
    if request.method == 'POST':
        producto = request.form.get('producto')
        categoria = request.form.get('categoria')
        existencia = request.form.get('existencia')
        precio = request.form.get('precio')
        return f"Producto: {producto}, Categoría: {categoria}, Existencia: {existencia}, Precio: {precio}"
    return render_template('productos.html')

# Formulario de registro de libros
@app.route('/libros', methods=['GET', 'POST'])
def libros():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        autor = request.form.get('autor')
        resumen = request.form.get('resumen')
        medio = request.form.get('medio')
        return f"Título: {titulo}, Autor: {autor}, Resumen: {resumen}, Medio: {medio}"
    return render_template('libros.html')

if __name__ == '__main__':
    app.run(debug=True)
