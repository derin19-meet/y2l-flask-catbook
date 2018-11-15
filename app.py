from flask import Flask
from flask import render_template
from database import *

app = Flask(__name__)

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def cat_profile(id):
    cat = cat_id_route(id)
    return render_template("cat.html", cat=cat)


@app.route('/form')
def form(name):
    form = add_new_cat(name)
    return render_template("form.html", form=form)



if __name__ == '__main__':
   app.run(debug = True)





