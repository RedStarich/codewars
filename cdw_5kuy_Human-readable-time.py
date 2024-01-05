def make_readable(seconds):
    hours = seconds//3600
    mins = seconds%3600//60
    sec = seconds - hours*3600 - mins*60
    
    h = str(hours)
    m = str(mins)
    s = str(sec)
    
    if len(h) == 1:
        h = '0' + h
    if len(m) == 1:
        m = '0' + m
    if len(s) == 1:
        s = '0' + s
    
    result = h + ':' + m + ':' + s
    return result