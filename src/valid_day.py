def valid_day(day):
    try:
        int_day = int(day)
        if int_day >= 1 and int_day <= 31:
            return int_day
    except:
        return None
    
print valid_day("2")