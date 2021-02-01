
'''
This is a python file for Checking the given number is prime number or not.
'''

def check_prime(number):
    '''
    Function to check for prime number.
    '''
    if number >= 1:
        for i in range(2, number):
            if (number % i) == 0:
                final_result="Not Prime"
            else:
                final_result="Prime"
    else:
        final_result="Not Prime"
    return final_result
