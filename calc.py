#!/usr/bin/python3

print('Welcome to Calculator')
def calculate():
    expression = input('Enter an expression: ')
    expression_result = check_input((expression).replace(' ', ''))
    while not expression_result:
        print('You did not enter a valid expression')
        expression = input('Enter an expression: ')
        expression_result = check_input((expression).replace(' ', ''))
    
    if expression_result:
        print(eval(expression_result))
    else:
        print("Expression result is False")
def check_input(input_expression):
    
    input_expression = str(input_expression)
    # Check the basics
    if len(input_expression) < 3:
        print('len is less than 3')
        return False
    # Check if we are getting passed correct characters
    for character in input_expression:
        if character not in '0123456789/*+-':
            print('{} not in given value'.format(character))
            return False
    # Things like /23 are not valid
    if input_expression[0] in '/*+':
        print('Are you sure you know what you\'re doing?')
        return False
    return input_expression
calculate()
while True:
    calc_again = input('''
        Do you want to calculate again?
        Please type Y for YES or N for NO.
        ''')
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
        break
    else:
        continue
