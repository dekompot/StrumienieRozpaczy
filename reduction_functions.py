import sys
import my_utilities as ut

def count_and_print_err_code(code) :
    print("Error code " + str(code) + " occurs " + str(count_if_err_code(code)) + " times.")

def count_if_err_code(code) :
    counter = 0
    for line in sys.stdin:
        if ut.get_err_code(line) == code : counter = counter + 1
    return counter

def sum_size_of_transfers() :
    sum = 0
    for line in sys.stdin:
        if ut.is_download(line) : sum += ut.get_transferred_data(line)
    return sum

def get_path_and_size_of_largest_file() :
    path = ""
    largest_size = 0
    for line in sys.stdin:
        if ut.get_transferred_data(line) > largest_size :
            largest_size = ut.get_transferred_data(line)
            path = ut.get_path(line)
    return path,largest_size

def get_graph_downloads_to_all_ratio() :
    all_downloads = 0
    graphics_downloads = 0
    for line in sys.stdin:
        if ut.is_download(line): 
            all_downloads+=1
            if ut.is_graphical_download(line) : graphics_downloads +=1
    return graphics_downloads / all_downloads