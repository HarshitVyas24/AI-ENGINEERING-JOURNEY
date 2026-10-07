dict= { # key : value
    "name" : "Harshit",
    "cgpa" : 9.2,
    "Subjects" : ["CN" , "COA", "DM"]

}

dict["cgpa"] = 9.8
print(dict["cgpa"])


# print(dict.keys())

keys_dict = list(dict.keys())
print(keys_dict)

print(type(keys_dict))


#methods

dict.keys()

dict.values()

dict.items()

# dict.get(val)  ----> better to use this instead of dict[key] as it gives no error if wrong key is used adn returns NONE

# dict.update(new_item)  ---->adds new item to the dict