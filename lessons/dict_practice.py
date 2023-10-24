"""Practice with Dictionaries!"""

#Constructing a dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Made my dictionary.")
print(ice_cream)

#Adding a key, value pair to a dictionary
ice_cream["mint"] = 3
print("After adding mint:")
print(ice_cream)

#Removing a key, value pair from a dictionary
ice_cream.pop("mint")
print("After removing mint:")
print(ice_cream)

#Accessing a value
#Will give error if use "" in f string, instead use ''
print(f"There are {ice_cream['chocolate']} orders of chocolate!")

#Adjusting a value
ice_cream["vanilla"] += 2
print("After adjusting amount of vanilla:")
print (ice_cream)

#Getting the length
#Length is telling you how many key value pairs you have
print(f"The number of key value pairs (ice cream flavors): {len(ice_cream)}")

#Check if a value is in a dictionary
print("Is chocolate in ice_cream?")
print("chocolate" in ice_cream)
print("Is mint in ice_cream?")
print("mint" in ice_cream)

#Using it in a conditional
if "mint" in ice_cream:
    print(f"There are number of orders: {ice_cream['mint']} of mint!")
else:
    print("No orders of mint.")

#Loop through and print out every flavor and its number of orders
print("Printing orders.")
for key in ice_cream:
    #print "<flavor> has <num_orders> orders."
    print(f"{key} has {ice_cream[key]} orders.")

