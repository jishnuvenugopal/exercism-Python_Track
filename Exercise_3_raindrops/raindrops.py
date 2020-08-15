def convert(number):
    raindrops=""
    if number % 3 == 0:
     raindrops +='Pling'
    if number % 5 == 0:
     raindrops +='Plang'
    if number % 7 == 0:
     raindrops +='Plong'
    if raindrops == '':
     return str(number)
    return raindrops
