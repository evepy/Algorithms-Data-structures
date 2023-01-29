#1)DEFINE EXPECTED BAKE TIME IN MINUTES( EXAMPLE :40 )
EXPECTED_BAKE_TIME = 40


def bake_time_remaining(time) -> int:
    """2)CALCULATE REMAINING BAKE TIME IN MINUTES:
    TIME EXPECTED - TIME REAL"""
    return EXPECTED_BAKE_TIME - time

def preparation_time_in_minutes(n_layers) -> int:
    """3)CALCULATE PREPARATION TIME IN MINUTES:
    LAYERS * MINUTES( EXAMPLE: 2 )"""
    return n_layers*2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time) -> int:
    """4)CALCULATE TOTAL ELPASED COOKING TIME { PREPARATION + BAKE }
    PD: PREPARATION TIME RECEIVES THE PREVIOUS FUNCTION -> preparation_time_in_minutes"""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
