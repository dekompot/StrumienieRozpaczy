import sys
from functools import partial
import utilities as ut

#filter function
def print_if(condition) :
    for line in sys.stdin:
        if condition(line) : print(line,end='')

#printing functions
def print_if_err_code(err_code) :
    print_if(partial (ut.err_code_equals,err_code))

def print_night() :
    print_if(partial (ut.was_downloaded_at_night))

def print_friday() :
    print_if(partial (ut.was_downloaded_on_friday))    
    
def print_polish() :
    print_if(partial (ut.was_downloaded_in_poland))      