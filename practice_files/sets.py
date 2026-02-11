
# Python lists = [] , sets = {} , and tuples = () practice

#  List  = [] ordered and changeable. Duplicates OK
#  Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#  Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# TIP: to get the commands available for lists you just print the variable for lists with dir Ex. print(dir(variable))
# another tip, for the description of the commands you can print the list but add help

# the tips applies for the 3 

games = ("skyrim", "oblivion", "kcd", "expedition 33", "kcd")

# games.pop()

print("skyrim" in games)

print(games.count("kcd"))

for game in games:
    print(game)