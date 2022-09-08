from flask import Flask,request,render_template,jsonify,redirect,url_for
from project_app.utils import Iris_Data
import config


app = Flask(__name__)

############################ POST MAN #####################################
# @app.route('/')

# @app.route('/predict',methods = ['GET','POST'])
# def predict():
#     data = request.form
    
#     SepalLengthCm = eval(request.form['SepalLengthCm'])
#     SepalWidthCm = eval(request.form['SepalWidthCm'])
#     PetalLengthCm = eval(request.form['PetalLengthCm'])
#     PetalWidthCm = eval(request.form['PetalWidthCm'])

#     iris = Iris_Data(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
#     result = iris.get_irisclass()
#     return jsonify({'Result ': f'The Predicted result is {result}'})

########################### WITH HTML PAGE ##################################


@app.route('/')
def main():
    return render_template('home.html')

@app.route('/predict',methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        SepalLengthCm = request.form['SepalLengthCm']
        SepalWidthCm = request.form['SepalWidthCm']
        PetalLengthCm = request.form['PetalLengthCm']
        PetalWidthCm = request.form['PetalWidthCm']

    iris = Iris_Data(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
    result = iris.get_irisclass()
    return render_template('after.html',result = result)

if __name__ == "__main__":
    app.run(host= '0.0.0.0',port= 5003,debug=False)