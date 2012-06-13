def valid_year(year):
    if year.isdigit():
        year = int(year)
        if year >= 1900 and year <= 2020:
            return year
        
print valid_year