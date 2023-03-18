from datetime import date

months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
http_get = "GET"
graphics_extensions = ['gif','jpg','jpeg','xbm']
success_code = 200

host_index = 0
date_time_index = 3
http_method_index = 5
path_index = 6
err_code_index = -2
data_index = -1

def get_host(line):
    return line.split()[host_index]

def get_host_extension(line):
    return get_host(line).split(".")[-1]

def get_date_time(line):
    return line.split()[date_time_index]

def get_date(line):
    return get_date_time(line).split(':')[0]

def get_day(line):
    return int(get_date(line).split("/")[0][1:])

def get_month(line):
    return months.index(get_date(line).split("/")[1].lower()) + 1

def get_year(line):
    return int(get_date(line).split("/")[2])

def get_weekday(line):
    return date(get_year(line),get_month(line),get_day(line)).weekday()

def get_time(line):
    return get_date_time(line).split(':')[1:]

def get_hour(line):
    return int(get_time(line)[0])

def get_http_method(line):
    return line.split()[http_method_index][1:]

def is_download(line):
    return get_err_code(line) == success_code and get_http_method(line) == http_get

def is_graphical_download(line):
    return get_extension(line) in graphics_extensions 

def get_path(line) :
    return line.split()[path_index]

def get_extension(line) :
    return get_path(line).split('.')[-1]

def get_err_code(line) :
    return int(line.split()[err_code_index])

def get_transferred_data(line) :
    try :
        return int(line.split()[data_index])
    except ValueError :
        return 0
