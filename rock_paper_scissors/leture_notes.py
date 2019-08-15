# Iterative solution for n = 2 and n = 3

# Variables for iterative solution
n = L
plays = [r, p, s]
result = []

# Iterative solution when n = 2
for play in plays:
    current = [play]
    for play in plays:
        current.append(play)
        result.append(current)
return result

# Iterative solution when n = 3
for play in plays:
    current = [play]
    for play in plays:
        current.append(play)
        for play in players:
            current.append(play)
            result.append(current)
return result

# The issue with an iterative solution is that for every n you need to add another for loop

# Recursion allows you to dynamically nest loops


def recursive_rps(options, n):
    if n == 1:
        return

    for option in options:
        options.append(option)
    options(result, n - 1)
