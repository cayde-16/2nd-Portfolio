#find out how many coins to give back
# 33 : 1 quarter(25), 1 nickel(5) 3 pennies (1)
#num_count(33)=>

def num_coins(cents):
    coins = {'Quarter': 25, 
            'nickel':5,
            'penny':1}

    if cents >= coins['Quarter']:
        cents = cents - coins['Quarter']

    return cents
    
