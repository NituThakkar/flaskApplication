from flask import Flask,render_template,request
import joblib

#initialse the app
app = Flask(__name__)
model = joblib.load('flask_app/dib_79.pkl')

@app.route('/')
def hello():
        return render_template('form.html')
        
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return 'contact page'

@app.route('/submit',methods=["POST"])
def form_data():
        preg = request.form.get('preg')
        plas = request.form.get('plas')
        pres = request.form.get('pres')
        skin = request.form.get('skin')
        test = request.form.get('test')
        mass = request.form.get('mass')
        pedi = request.form.get('pedi')
        age = request.form.get('age')

        output=model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
        print(output)
        if output[0] == 1:
         out = 'diabatic'
        else:
            out = 'not diabatic'

        # return render_template('index.html',data=(preg,plas,pres,skin,test,mass,pedi,age))
        return render_template('predict.html' , data = f'person is {out}')


if __name__=='__main__':
    app.run(debug=True)

