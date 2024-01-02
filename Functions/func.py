import sys

from StringFunc import string_Execution as se
from list import list as le
class Function:
    while True:
        option = input('Enter the function to proceess:')
        if option == 'String':
            print('String Function calls')
            se()
        elif option == 'List':
            le()
        elif option == 'exit':
            sys.exit()
        else:
            print('Please Enter the Correct Function')



f = Function()
