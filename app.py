from flask import Flask, render_template, request, redirect, url_for, abort

taches = [ 
    {"id": 1, "titre": "Réviser les décorateurs", 
     "priorite": "haute", "terminee": False}, 
    {"id": 2, "titre": "Installer Flask", 
     "priorite": "normale", "terminee": True}, 
    {"id": 3, "titre": "Lire la doc Jinja2", 
     "priorite": "basse", "terminee": False},
    {"id": 4, "titre": "<b>Important</b>", 
     "priorite": "normale", "terminee": False}
]

app = Flask(__name__)

## Mission 1
# @app.route('/')
# def index():
#     return "<h1>Mes tâches</h1>" + "pour L3"


## Mission 2
@app.route("/taches/<int:id>") 
def tache(id):
    print(type(id), id)
    for t in taches: 
        if t["id"] == id: 
            return t["titre"] 
    abort(404)


## Mission 3
@app.route("/")
def index():
    return render_template("taches.html", taches=taches)

@app.route("/taches/ajouter", methods=["GET", "POST"])
def ajouter():
    if request.method == "POST":
        titre = request.form.get("titre", "").strip()
        priorite = request.form.get("priorite", "")

        if not titre or len(titre) > 80 or priorite not in ("basse", "normale", "haute"):
            return render_template(
                "ajouter.html",
                titre=titre,
                priorite=priorite,
                erreur="Le titre doit contenir entre 1 et 80 caractères",
            )

        nouvel_id = max((t["id"] for t in taches), default=0) + 1
        taches.append({"id": nouvel_id, "titre": titre,
                       "priorite": priorite, "terminee": False})
        return redirect(url_for("index"))
    return render_template("ajouter.html", titre="", priorite="normale")