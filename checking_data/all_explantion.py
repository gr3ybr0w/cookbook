# demonstrates for to use any and all


all([x in [1, 2, 3, 4, 5] for x in [3, 4, 5]])
# all([true, true, true])
# true and true and true = true


all([x in [1, 2, 3, 4, 5] for x in [3, 4, 8]])
# all([true, true, false])
# true and true and false = false


any([x in [1, 2, 3, 4, 5] for x in [3, 4, 8]])
# any([true, true, false])
# true or true or false = true

all([x % 2 == 0 for x in [22, 4, 6, 8]])
