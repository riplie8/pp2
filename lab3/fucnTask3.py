def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits
    return chickens, rabbits

c, r = solve(76, 170)
print("chickens:", c, "rabbits:", r)
