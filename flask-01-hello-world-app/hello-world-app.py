from flask import Flask 
app = Flask(__name__)
@app.route('/')
def head():
    return 'Hello World!'
@app.route('/second')

def second():
    return 'This is the second page'
@app.route('/third/subthird')

def third():
    return 'This is the subpage of third page'





if __name__ == '__main__':

    app.run(debug=True, port=30000)
    # app.run(host= '0.0.0.0', port=8081)