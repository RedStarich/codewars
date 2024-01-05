def get_pins(observed):
    hm = {'1':['2','4'], 
          '2':['1','3','5'], 
          '3':['2','3','6'], 
          '4':['1','5', '7'], 
          '5':['2','4','6','8'], 
          '6':['3','5','9'], 
          '7':['4', '8'], 
          '8':['5','7','9','0'], 
          '9':['6', '8'],
          '0':['8']
         }
    
    import itertools
    combinations = [[num]+hm[num] for num in observed]
        
    return [''.join(element) for element in set(itertools.product(*combinations))]