from flask import render_template,redirect,request,session,flash  

from flask_app import app

from flask_app.models import dojo

@app.route('/')
def dojos_index():
  return render_template("index.html")

@app.route('/create/dojo',methods=['POST'])
def dojos_create():
    data = {
        "name":request.form['name'],
    }
    dojo.Dojo.dojo_save(data)
    return redirect('/dojos')



@app.route('/dojos')
def dojos():
  return render_template("index.html",all_dojos=dojo.Dojo.dojo_get_all())


# @app.route('/show/<int:dojo_id>')
# def dojos_detail_page(dojo_id):
#     data = {
#         'id': dojo_id
#     }
#     return render_template("details_page.html",dojo=dojo.Dojo.get_one(data))

@app.route('/dojo/<int:dojo_id>')
def dojos_edit_page(dojo_id):
    data = {
        'id': dojo_id
    }
    return render_template("dojo.html", dojo = dojo.Dojo.dojo_get_one(data))

@app.route('/update/<int:dojo_id>', methods=['POST'])
def dojos_update(dojo_id):
    data = {
        'id': dojo_id,
        "name":request.form['name'],
    }
    dojo.Dojo.update(data)
    return redirect(f"/dojo/{dojo_id}")

# @app.route('/delete/<int:dojo_id>')
# def dojos_delete(dojo_id):
#     data = {
#         'id': dojo_id,
#     }
#     dojo.Dojo.destroy(data)
#     return redirect('/dojos') 