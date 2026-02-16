

games = {"Skyrim": "Bethesda" ,
         "League": "Riot" ,
         "KCD": "Warhorse" ,
         "CSGO": "Valve"}

#games.update({"CS2": "VALVE AGAIN"})
#games.update({"KCD": "WARHOSE STUDIOS"})
# games.pop("CSGO")
# print(games.get("KCD2"))

#if games.get("CS2"):
    #print("nigger")
#else:
    #print("nigeria")


gameskeys = games.keys()

for keys in games.keys():
    print(keys)

gameitems = games.items()
#print(gameitems)

for key, value in games.items():
    print(f"{key}: {value}")



#print(gameskeys)
#print(games)