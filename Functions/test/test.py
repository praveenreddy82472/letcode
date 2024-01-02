from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/string',methods=['GET','POST'])
def string_Execution():
    if request.method == 'POST':
        s = request.form("s")
        option = request.form("option")
        if request.form(option == 'find'):
            option1= request.form(s.find("option1"))
            result = option1
        return result

if __name__ == "__main__":
    app.run(debug=True)