programming_dictionary={
    "Bug":"An error in the program that prevents the program from running as expected",
"Function":"Code that you can call again and again",
}
# print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "Action of doing something again and again"

# empty_dictionary={}
# #wipe 
# programming_dictionary={}
# print(programming_dictionary)

#edit
# programming_dictionary["Bug"] = "Similar to error"
# programming_dictionary["Bugs"] = "too many errors"
# print(programming_dictionary)

# #loop
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

#remove item
# del programming_dictionary["Loop"]
# print(programming_dictionary)

# for value in programming_dictionary.values():
#     print(value)

# for key, value in programming_dictionary.items():
#     print(key,value)

#Nesting Dictionary
capitals={
    "France":"Paris",
    "Germany":"Berlin"
}
# travel_log={
#     "France":["Paris", "Lille","Dijon"],
#     "Germany":["Stu","Berlin"]
# }
# print(travel_log["France"][1])

# nested_list=["A","B",["C","D"]]
# print(nested_list[2][1])

travel_log={
    "France":{
        "num_times_visited":8,
        "cities_visited":["Paris", "Lille","Dijon"],
    },
    "Germany":{
        "num_times_visited":8,
        "cities_visited":["Stu","Berlin"],
    },
}

print(travel_log["Germany"]["cities_visited"][1])