from flask import Flask, render_template, request
import models as dbHandler


app = Flask(__name__)

app.config['MAIL_SERVER'] = 'correo.silvopastoril2019.org.py'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/normas')
def normas():
   return render_template('normas.html')

@app.route('/galeria')
def galeria():
   return render_template('galeria.html')
   
@app.route('/registro', methods=['POST', 'GET'])
def registro():
   if request.method=='POST':
      name = request.form['nombre']
      document = request.form['tipo_documento']
      n_document = request.form['numero_documento']
      mail = request.form['email']
      country = request.form['pais']
      city = request.form['ciudad']
      address = request.form['direccion']
      phone = request.form['telefono']
      institute = request.form['institucion']
      ocupation = request.form['ocupacion']
      participation = request.form['tipo_participacion']
      ponencia = request.form['ponencia']
      english = request.form['ingles']
      coments = request.form['comentarios']
      social = request.form['nombre_razon_social']
      ruc = request.form['ruc']
      if ponencia == '':
         ponencia = None
      if english == '':
         english = None
      if social == '':
         social = None
      if ruc == '':
         ruc = None
      dbHandler.insertdata(name, document, n_document, mail, country, city, address, phone, institute, ocupation, participation, ponencia, english, coments, social, ruc)
      if request.form['ocupacion'] == 'Estudiante Nacional' or request.form['ocupacion'] == 'Estudiante Extranjero':
         return render_template('redirect.html')
      if request.form['ocupacion'] == 'Profesional Nacional':
         return render_template('redirect1.html')
      else:
         return render_template('redirect2.html')
   else:
      return render_template('formulario.html')

@app.route('/form', methods=['POST', 'GET'])
def register():
   if request.method=='POST':
      name = request.form['nombre']
      document = request.form['tipo_documento']
      n_document = request.form['numero_documento']
      mail = request.form['email']
      country = request.form['pais']
      city = request.form['ciudad']
      address = request.form['direccion']
      phone = request.form['telefono']
      institute = request.form['institucion']
      ocupation = request.form['ocupacion']
      participation = request.form['tipo_participacion']
      ponencia = request.form['ponencia']
      english = request.form['ingles']
      coments = request.form['comentarios']
      social = request.form['nombre_razon_social']
      ruc = request.form['ruc']
      if request.form['ponencia'] == '':
         ponencia = None
      if request.form['ingles'] == '':
         english = None
      if request.form['nombre_razon_social'] == '':
         social = None
      if request.form['ruc'] == '':
         ruc = None
      dbHandler.insertdata(name, document, n_document, mail, country, city, address, phone, institute, ocupation, participation, ponencia, english, coments, social, ruc)
      if request.form['ocupacion'] == 'Estudiante Nacional' or request.form['ocupacion'] == 'Estudiante Extranjero':
         return render_template('redirect.html')
      if request.form['ocupacion'] == 'Profesional Nacional':
         return render_template('redirect1.html')
      else:
         return render_template('redirect2.html')
   else:
      return render_template('form.html')

"""@app.route('/redirect')
def redirect():
   return render_template('redirect.html')"""

@app.route('/homei')
def homei():
   return render_template('index-e.html')

@app.route('/homei/norms')
def norms():
   return render_template('normas-e.html')

@app.route('/homei/gallery')
def gallery():
   return render_template('galeria-e.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)
