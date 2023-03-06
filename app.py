from flask import Flask,render_template

app= Flask(__name__)


@app.route("/")
def index():
    data={
        "titulo":"Pagina de libros",
        "encabezado":"Bienvenido"
    }
    return render_template("index.html",data=data)

@app.route("/suma/<int:valor1>/<int:valor2>")
def suma(valor1,valor2):
    return "La suma es {0}".format((valor1+valor2))

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return "Hola {0}".format(nombre)

@app.route("/contacto")
def contacto():
    data={
        "titulo":"contacto",
        "encabezado":"Bienvenido"
    }
    return render_template("contacto.html",data=data)

if __name__=="__main__":
    app.run(debug=True)