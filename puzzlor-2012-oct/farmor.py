""" Calculate the possibilities for the October 2012 PuzzlOR puzzle. """

# information for each crop
CORN = {'fertilizer_cost': 30000, 'profit': 190000,
        'insurance_cost': 35000, 'name': 'corn', 'loss': -190000}
SOYBEANS = {'fertilizer_cost': 10000, 'profit': 170000,
            'insurance_cost': 20000, 'name': 'soybeans', 'loss': -170000}

# all possible decision permutations
COMBINATIONS = [(c, i, f)
                for c in (CORN, SOYBEANS)
                for i in (False, True)
                for f in (False, True)]

# format for output
FORMAT = '$%0.2f \t (Plant: %s, Insurance: %s, Fertilizer: %s)'


def prob_success(insurance, fertilizer):
    """ Return probability of success in harvesting the crop. """
    if insurance and fertilizer:
        return 1
    elif insurance:
        return 0.9
    elif fertilizer:
        return 0.95
    else:
        return 0.85


def expected_value(crop, insurance=0, fertilizer=0):
    """ Return expected value given success or failure. """
    p_success = prob_success(insurance, fertilizer)
    costs = insurance * crop['insurance_cost'] + fertilizer * crop['fertilizer_cost']
    profits = crop['profit'] * p_success + crop['loss'] * (1 - p_success)
    return profits - costs


def get_all():
    """ Return results for every decision permutation. """
    for crop, insurance, fertilizer in COMBINATIONS:
        expected = expected_value(crop, insurance, fertilizer)
        print FORMAT % (expected, crop['name'], bool(insurance), bool(fertilizer))


if __name__ == '__main__':
    get_all()
