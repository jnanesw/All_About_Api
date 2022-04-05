from distutils.log import debug
from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route('/math_ope',methods=['POST'])
def Math_operation():
    if(request.method=='POST'):
        operation=request.json['operation']
        a=request.json['num1']
        b=request.json['num2']
        if(operation=='Add'):
            result="Addition of "+str(a)+" and "+str(b)+" is: "+str(a+b)
        if(operation=='Subtract'):
            result="Subtraction of "+str(a)+" and "+str(b)+" is: "+str(a-b)
        if(operation=='Multiplication'):
            result="Multiplication of "+str(a)+" and "+str(b)+" is: "+str(a*b)
        if(operation=='Division'):
            result="Division of "+str(a)+" and "+str(b)+" is: "+str(a//b)
        return result

if(__name__=="__main__"):
    app.run(debug=True)