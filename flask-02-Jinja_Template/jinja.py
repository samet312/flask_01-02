from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    
    return render_template('index.html', number1=1234, number2=7896)

@app.route('/cohort16')
def cohort():
    value1, value2 = 23, 45
    return render_template('body.html',val1=value1 , val2=value2 ,sum = value1+value2)






if __name__== "__main__":
    app.run(debug=True, port=30000)
    # app.run(host= '0.0.0.0', port=8081)