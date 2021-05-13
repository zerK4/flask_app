from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__,template_folder='./templates',static_folder='./templates/static')
app.secret_key = "hello"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/planuri")
def planuri():
    return render_template("planuri.html")
@app.route("/pasi")
def pasi():
    return render_template("pasi.html")
@app.route("/intrebari")
def intrebari():
    return render_template("intrebari.html")
@app.route("/politica")
def politica():
    return render_template("politica.html")

#testing
@app.route("/testing", methods=["POST", "GET"])
def test():
    if request.method == "POST":
        user = request.form["firstname"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for(test))
        return render_template("test.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1> {user} </h1>"
    else:
        return redirect(url_for("testing.html"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("user"))

if __name__ == "__main__":
    app.run(debug=True)