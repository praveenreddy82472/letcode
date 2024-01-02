def list():
    s = eval(input('Enter the word|senance|para:'))
    while True:
        option = input('Enter the function name:')
        if option == 'emptylist':
            pass
        elif option == 'input':
            print(eval(input('Enter the list:')))
        elif option == 'split':
            print(s.split())
        elif option == "":
            pass
        elif option == 'exit':
            break
        else:
            print('Please Enter the Correct Function')
