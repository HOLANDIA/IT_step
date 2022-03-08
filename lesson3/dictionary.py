my_dic = {
    "name": "sandro",
    "surname": "iremadze",
    "age": 23,
    "location": "tbilsi",
    "children": ["mariami", "emilia", "gio"]    # value-ს აქვს სიის სახეეც
}

my_dic["age"] = 33
my_dic["has_gf"] = True
my_dic.pop("location")
print(my_dic)
my_dic.clear()
print(my_dic)