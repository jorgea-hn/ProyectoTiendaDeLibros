from flask import Flask,render_template,request

app= Flask(__name__)

@app.before_request
def before_request():
    print("Antes de la peticion")

@app.after_request
def after_request(response):
    print("Despues de la peticion")
    return response

@app.route("/")
def index():
    print("Entrando a la vista")
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


@app.route("/lenguajes")
def lenguajes():
    data={
        "hay_lenguajes":False,
        "lenguajes": ["PHP","Python","HTML5 ","CSS3","Java","JavaScript"]}
    return render_template("lenguajes.html",data=data)


@app.route("/datos")
def datos():
    # print(request.args)
    valor1= request.args.get("valor1")
    return "Estos son los datos: {0}".format(valor1)

@app.route("/contacto")
def contacto():
    data={
        "titulo":"contacto",
        "encabezado":"Bienvenido"
    }
    return render_template("contacto.html",data=data)

if __name__=="__main__":
    app.run(debug=True)