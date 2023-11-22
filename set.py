# set is collection which is unordered, unindexed. no duplicate values


utensils = {"fork", "spoon", "spoon","knife"}
dishes = {"bowl", "plate", "cup"}
utensils.add("napkins")
# utensils.remove("spoon")
# utensils.clear()
collection = {"fuck you freak"}
# collection.update(dishes,utensils)
collection_fucker = utensils.union(dishes)
print("Collection Fuckers")
print("Fucker Dish:")
print(dishes.difference(utensils))
print("Fucker Utensil:")
print(utensils.difference(dishes))
