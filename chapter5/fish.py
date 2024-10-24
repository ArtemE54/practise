sea_fish        = ["shark", "flounder", "tuna", "cod", "herring", "Marlin"] 
freshwater_fish = ["Asp", "Pike", "Carp", "Salmon", "Ide", "Trout"]

all = sea_fish + freshwater_fish
all.sort(key=str.lower)
print(all)
