import logs_functions as lf

NIGHT_BEGINNING = 22 #bigger than NIGHT_END
NIGHT_END = 6 #smaller than NIGHT_BEGINNING
FRIDAY_INDEX = 4
POLISH_DOMAIN_EXTENSION = 'pl'

def err_code_equals(error_code, line) :
    return lf.get_err_code(line) == error_code

def was_downloaded_at_night(line) :
    return lf.is_download(line) and (lf.get_hour(line) < NIGHT_END or lf.get_hour(line) >= NIGHT_BEGINNING)

def was_downloaded_on_friday(line) :
    return lf.is_download(line) and lf.get_weekday(line) == FRIDAY_INDEX

def was_downloaded_in_poland(line) :
    return lf.is_download(line) and lf.get_host_extension(line) == POLISH_DOMAIN_EXTENSION