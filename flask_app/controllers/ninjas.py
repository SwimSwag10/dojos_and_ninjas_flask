from flask import render_template,redirect,request,session,flash  

from flask_app import app

from flask_app.models import ninja, dojo

@app.route('/create/ninja',methods=['POST'])
def create():
    print("************************", request.form)

    data = {
        "dojo_id" : request.form['dojo_id'],
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "age":request.form['age'],
    }
    ninja.Ninja.ninja_save(data)
    dojo_id = request.form['dojo_id']
    return redirect(f'/dojo/{dojo_id}')




@app.route('/ninjas')
def ninjas():
    return render_template("ninja.html",dojos=dojo.Dojo.dojo_get_all())


# @app.route('/show/<int:ninja_id>')
# def detail_page(ninja_id):
#     data = {
#         'id': ninja_id
#     }
#     return render_template("details_page.html",ninja=ninja.Ninja.get_one(data))

# @app.route('/edit_page/<int:ninja_id>')
# def edit_page(ninja_id):
#     data = {
#         'id': ninja_id
#     }
#     return render_template("edit_page.html", ninja = ninja.Ninja.get_one(data))

# @app.route('/update/<int:ninja_id>', methods=['POST'])
# def update(ninja_id):
#     data = {
#         'id': ninja_id,
#         "first_name":request.form['first_name'],
#         "last_name":request.form['last_name'],
#         "age":request.form['age'],
#     }
#     ninja.Ninja.update(data)
#     return redirect(f"/show/{ninja_id}")

# @app.route('/delete/<int:ninja_id>')
# def delete(ninja_id):
#     data = {
#         'id': ninja_id,
#     }
#     ninja.Ninja.destroy(data)
#     return redirect('/ninjas')