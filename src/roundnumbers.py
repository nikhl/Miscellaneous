def round(n):
    n_str = str(n)
    decimal = n_str.find('.')
    tenths = n_str[decimal+1:decimal+2]
    integer = n_str[0:decimal]
    if int(tenths) >= 5:
        return int(integer) + 1
    else:
        return int(integer)
    
    
print round(32.49)
print round(32.56)
print round(0.0)
print round(99.50)