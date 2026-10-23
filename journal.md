Mission 1 : 19:35
1. a. après lancement de flask --app app run il affiche sur chrome ce que la fonction index à en return c'est a dire qu'il affiche l'en-tête "Mes tâches"
1. b. j'ai modifier le texte en "Mes tâches pour L3" et j'ai recharger la page et j'ai remarqué que le texte de la page ne change pas. les modifications faites n'apparaîssent pas.

##############################################################################################################################

19:41
2. lancement du serveur avec flask --app app run --debug et le termial affiche Debug is active et quand je fais des modifications il affiche "Detected change in 'C:\\UPA\\L3\\S5\\Développement avancé\\tp\\TP2\\tp2-flask-taches\\app.py', reloading". Sur chrome les modification apparaissent.

##############################################################################################################################

19:48
3. Erreur volontaire sur "<h1>Mes tâches</h1>" + 1 et le terminal affiche "TypeError: can only concatenate str (not "int") to str". Pour corriger l'erreur j'ai remplacer "1" qui était de type int par un texte qui était de type str, et l'erreur a disparu

##############################################################################################################################

19:56
4. même sans mettre --app dans flask run --debug il fonctionne toujours car le projet reconnais automatiquement notre fichier app, fonctionnel seulement quand le fichier s'appel app.py

##############################################################################################################################

20:04
En mode debug, le serveur redémarre à chaque modification de fichier et affiche les erreurs détaillées dans le navigateur

##############################################################################################################################

Mission 2 :
20:15
1. integration des ligne de code dans app et la page affiche "tache introuvable". 

------------------------------------------------------------------------------------------------------------------------------

20:23
2. insertion de print(type(id), id) dans la focntion et le terminal affiche "<class 'int'> 2"

------------------------------------------------------------------------------------------------------------------------------

20:25
3. lors de la visite de la tâche/2 il affiche "installer flask" et renvoie un 200 sur le terminal
   lors de la visite de la tache/abc il affiche "not found" et renvoie une erreur 404 sur le terminal

------------------------------------------------------------------------------------------------------------------------------

20:30
4. lors de la visite de la page tache/2/ il affcihe "Not found" et le terminal affiche une erreur 404

------------------------------------------------------------------------------------------------------------------------------

20:35
5. visite de la page tache/99 il affiche tache introuvable mais sur F12 il affcihe un status 200

------------------------------------------------------------------------------------------------------------------------------

20:43
6. visite de la page tache/99 avec abort404 il affiche une page Not Found suivi du status 404

------------------------------------------------------------------------------------------------------------------------------

explication : 
la tache 2 est introuvable avec <id> car il était de type str hors que l'on cherche un int.
"int: " transforme le str en type entier.
Selon moi, la barre oblique final provoque une erreur 404

------------------------------------------------------------------------------------------------------------------------------

Mission 3: 13:28 (vendredi)
3. {{ loop.index }} permet de concatenner des chiffres en commençant par 1.
   {{ t.titre|upper }} permet de mettre le texte en uppercase
   {{ t.titre|length }} permet d'obtenir la taille de chaque titre
   {{ t.titre|sort(attribute="titre") }} affiche chaque caractère dans un " '' " séparé d'une virgule.
   résultat obtenu : ['R', 'é', 'v', 'i', 's', 'e', 'r', ' ', 'l', 'e', 's', ' ', 'd', 'é', 'c', 'o', 'r', 'a', 't', 'e', 'u', 'r', 's']

5. insertion de <p>{{ inconnue }}</p> dans base.html et la page n'affiche pas d'erreur

6. l'insertion de <b>Important</b> ne le met pas en gras

explication :
{{ … }} permet d'afficher une valeur et {% … %} est utiliser dans les boucles

Mission 4: 15:28

{% extends %} permet de faire une héritage. il hérite de la classe parent qui est base.html
le texte écrit hors du blocs 
{{ super() }} insère le contenu du bloc du parent à l’intérieur du bloc enfant
templates est recherhé grâce a render _template de flask

Mission 5 :15:51

1. a chaque fois que l'on fait F5 il demande une validation pour le pop-up de Confirmer le nouvel envoi du formulaire et le nombre de tache s'ajoute.
   elle apparait a chaque fois que l'on actualise la page

2. url : http://127.0.0.1:5000/taches/ajouter
   Méthode : POST

3. avec redirect(url_for("index")), après l'ajout de tache, il n'affiche pas le pop-up de confirmation t j'ai juste qu'a actualiser la page pour avoir de nouveaux taches
par contre url et la méthode sont similaire:
   url : http://127.0.0.1:5000/taches/ajouter
   Méthode : POST

quand j'ai mis request.form["titr"] il n'a pas reconnu "titr"

6. quand j'ai retirer la méthohde post de ajouter.html, dans la barre du navigateur il a affciher http://127.0.0.1:5000/taches/ajouter?titre=azertyui&priorite=normale

Expliqué :
On redirige après un formulaire traité car sans cela F5 rejoue le POST et crée un doublon. Avec redirect, le serveur répond 302 et le navigateur fait un GET ; F5 ne rejoue que ce GET.
request.form.get("titre") renvoie None (ou la valeur par défaut) si le champ est absent ; request.form["titre"] provoque une erreur 400 Bad Request. Les données d'un formulaire en GET partent dans l'URL, après le ?, visibles dans la barre d'adresse et conservées dans l'historique.
