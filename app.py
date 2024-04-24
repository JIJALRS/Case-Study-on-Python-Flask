from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import pickle
app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/Prediction',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        Gend = request.form['Gender']
        Age=float(request.form['Age'])
        Sal=float(request.form['Salary'])
        Gen=[]
        if Gend=="Female":
            Gen=0
        else:
            Gen=1 
        
        data={"Age":Age,"EstimatedSalary":Sal,'Gender':float(Gen)}
        data=pd.DataFrame(data,index=[0])
        pickled_model = pickle.load(open('model.pkl','rb'))
        result=pickled_model.predict(data)[0]
        print(result)
        

    return render_template('prediction.html',result=result)

if __name__=='__main__':
    app.run()