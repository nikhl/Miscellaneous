# takes as input any text and if it the name of a month, the following script returns it in a neatly formatted way

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
def valid_month(month):
    if month != None and len(month) > 1:
        list_month = list(month)
        first_char = [x.upper() for x in list_month[0]]
        rem_letters = [x.lower() for x in list_month[1:]]
        modified_month = "".join(first_char+rem_letters)
        if modified_month in months:
            return modified_month
        else:
            return None
    else:
        return None
    
print valid_month("January")

#another way
#def valid_month(month):
#    if month:
#        cap_month = month.capitalize()
#        if cap_month in months:
#            return cap_month
