import sys
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/string')
def string_Execution():
    s = request.form(input('Enter the word|senance|para:'))
    print('String Function Executed')
    while True:
        option = request.form(input('Enter the function name:'))
        if request.form(option == 'find'):
            print(s.find(input('Enter the word to find:')))
        elif request.form(option == 'index'):
            print(s.index(input('Enter the word to get index position:')))
        elif request.form(option == 'count'):
            print(s.count(input('Enter the word to count number of times a word can occurs:')))
        elif request.form(option == 'strip'):
            print(s.strip())
        '''elif request.form(option == 'rstrip'):
            print(s.rstrip())
        elif option == 'lstrip':
            print(s.lstrip())
        elif option == 'split':
            print(s.split())
        elif option == 'replace':
            print(s.replace(input('Enter the old word'),input('Enter the new Word to Replace:')))
        elif option == 'join':
            print(s.join(input('Enter the word|sysmbol to join:')))
        elif option == 'lower':
            print(s.lower())
        elif option == 'upper':
            print(s.upper())
        elif option == 'title':
            print(s.title())
        elif option == 'capital':
            print(s.capitalize())
        elif option == 'swapcase':
            print(s.swapcase())
        elif option == 'startswith':
            print(s.startswith(input('Enter the word to check start word:')))
        elif option == 'endswith':
            print(s.endswith(input('Enter the word to check start word:')))
        elif option == 'islower':
            print(s.islower())
        elif option == 'isupper':
            print(s.isupper())
        elif option == 'isalpha':
            print(s.isalpha())
        elif option == 'isalphanum':
            print(s.isalnum())
        elif option == 'isspace':
            print(s.isspace())
        elif option == 'isdigit':
            print(s.isdigit())
        elif option == 'istitle':
            print(s.istitle())
        elif option == 'format':
            print(s.format())'''
        elif option == 'exit':
            break


        else:
            print('Please enter the correct function')

if __name__ == "__main__":
    app.run(debug=True)