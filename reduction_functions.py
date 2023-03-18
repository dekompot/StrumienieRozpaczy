import sys
from functools import partial
import logs_functions as lf
import utilities as ut

def count_and_print_err_code(code) :
    print("Error code " + str(code) + " occurs " + str(count_if_err_code(code)) + " times.")

# reduction functions
def count_if(condition) :
    counter = 0
    for line in sys.stdin:
        if condition(line) : counter = counter + 1
    return counter

def sum_if(condition,get_value) :
    sum = 0
    for line in sys.stdin:
        if condition(line) : sum = sum + get_value(line)
    return sum

def get_max_line(get_value) :
    max = 0
    max_line = ""
    for line in sys.stdin:
        if get_value(line) > max : max = get_value(line) ; max_line = line
    return max_line

#specified reduction functions
def count_if_err_code(error_code) :
    return count_if(partial(ut.err_code_equals,error_code)) 

def sum_if_transfer_data() :
    return sum_if(partial(lf.is_download),partial(lf.get_transferred_data))

def get_largest_file() :
    return get_max_line(partial (lf.get_transferred_data))

def get_path_and_size_of_largest_file() :
    max_line = get_largest_file()
    return lf.get_path(max_line), lf.get_transferred_data(max_line)
"""
def get_graph_downloads_to_all_downloads_ratio():
    return count_if_is_graphical_download() / count_if_is_download ()
"""

def get_graph_downloads_to_all_ratio() :
    all_downloads = 0
    graphics_downloads = 0
    for line in sys.stdin:
        if lf.is_download(line): 
            all_downloads+=1
            if lf.is_graphical_download(line) : graphics_downloads += 1
    return graphics_downloads / all_downloads



