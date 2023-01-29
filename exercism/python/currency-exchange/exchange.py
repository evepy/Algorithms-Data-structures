def exchange_money(budget, exchange_rate) -> float:
    return budget / exchange_rate

def get_change(budget, exchanging_value) -> float:
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills) -> int:
    return denomination * number_of_bills

def get_number_of_bills(budget, denomination) -> int:
    return budget // denomination

def get_leftover_of_bills(budget, denomination) -> float:
    return budget % denomination

def exchangeable_value(budget, exchange_rate, spread, denomination) -> int:
    #Falta 
    return (budget - denomination) / (exchange_rate + (exchange_rate * spread / 100))