from flask import Flask, render_template, request, jsonify
import StringFunc as se
app = Flask(__name__)

@app.route('/')
def post_method():
    if (request.method=='POST'):
      option = request.form['option']
      word = request.form['word']
      option1 = request.form['option1']
      if(option == 'string'):
          result = f'word {word} to find {option1}'
          return result

if __name__ == "__main__":
    app.run(debug=True)




