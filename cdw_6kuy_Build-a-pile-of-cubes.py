def find_nb(m):
    
    cube = 0
    vol = 0
    
    while (vol < m):
        vol += cube**3
        cube += 1
    
    if vol == m:
        return cube-1
    else:
        return -1