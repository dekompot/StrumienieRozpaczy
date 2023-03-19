from datetime import date

MONTHS = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
HTTP_GET = "GET"
GRAPHICS_EXTENSION = ['gif','jpg','jpeg','xbm']
SUCCESS_CODE = '200'

HOST_INDEX = 0
DATE_TIME_INDEX = 3
HTTP_METHOD_INDEX = 5
PATH_INDEX = 6
ERR_CODE_INDEX = -2
DATA_INDEX = -1

def get_host(line):
    return line.split()[HOST_INDEX]

def get_host_extension(line):
    return get_host(line).split(".")[-1]

def get_date_time(line):
    return line.split()[DATE_TIME_INDEX]

def get_date(line):
    return get_date_time(line).split(':')[0]

def get_day(line):
    return int(get_date(line).split("/")[0][1:])

def get_month(line):
    return MONTHS.index(get_date(line).split("/")[1].lower()) + 1

def get_year(line):
    return int(get_date(line).split("/")[2])

def get_weekday(line):
    return date(get_year(line),get_month(line),get_day(line)).weekday()

def get_time(line):
    return get_date_time(line).split(':')[1:]

def get_hour(line):
    return int(get_time(line)[0])

def get_http_method(line):
    return line.split()[HTTP_METHOD_INDEX][1:]

def is_download(line):
    return get_err_code(line) == SUCCESS_CODE and get_http_method(line) == HTTP_GET

def is_graphical_download(line):
    return get_extension(line) in GRAPHICS_EXTENSION 

def get_path(line) :
    return line.split()[PATH_INDEX]

def get_extension(line) :
    return get_path(line).split('.')[-1]

def get_err_code(line) :
    return line.split()[ERR_CODE_INDEX]

def get_transferred_data(line) :
    try :
        return int(line.split()[DATA_INDEX])
    except ValueError :
        return 0
