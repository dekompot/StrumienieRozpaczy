import my_utilities as ut
import sys

def print_if_err_code(code) :
    for line in sys.stdin:
        if ut.get_err_code(line) == code : print(line,end='')

def print_night() :
    for line in sys.stdin:
        if ut.is_download(line) and (ut.get_hour(line) < 6 or ut.get_hour(line) >= 22) : print(line,end='')

def print_friday() :
    for line in sys.stdin:
        if ut.is_download(line) and ut.get_weekday(line) == 4 : print(line,end='')        

def print_polish() :
    for line in sys.stdin:
        if ut.get_host_extension(line) == 'pl' : print(line,end='')
