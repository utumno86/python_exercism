EXPECTED_BAKE_TIME = 40


def bake_time_remaining(time_in_oven):
    """
    Return expected bake time remaining.

    This function takes the amount of time the lasagna has been in the oven and subtracts it from the expected bake time.
    """
    return EXPECTED_BAKE_TIME - time_in_oven


def preparation_time_in_minutes(layers):
    """
    Return preperation time.

    This function takes a number representing the number of layers and multiplies it by the time spent to complete the layers
    """
    return 2 * layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)
