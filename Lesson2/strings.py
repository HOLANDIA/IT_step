name = "sandro"
# # რეალურად ყველა სტრინგი შეგვიძლია მივიჩნიოთ char(ასო, character) ტიპის ელემენტებისგან შემდგარ საიდ


# # დავპრინტპოთ ნებისმიერი ასო სტრინგიდან
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])


# # დავთვალეთ სტრინგის სიგრძე
# print(len(name))


# # შევამოწმოთ რაიმე ელემენტის არსებობა მოცემულ სტრინგში
print("o" in name)   # bool-ის ტიპის ბრძანება 


# # slicing(ჩამოჭრა) 
surname = "iremadze"
# print(surname[2:5])   
# print(surname[:3])
# print(surname[5:])

# # negative index 
print(surname[-6:]) 




# surname = "iremadze"
#print(surname.capitalize())  # პირველი ასოს გადიდება 
#print(surname.upper())  # ყველა ასოს გადიდება


# name = "    sandro"
# surname = "iremadze"
# print(name.strip())   # strip აშორებს სტრინგს ზედმეტ space-ებს



# # დავშალოთ წინადადება სიტყვებად და შევქმნათ მათგან სია

# my_text = "i love georgia"
# print(my_text.split())   # split - დაყოფა, გახლეჩვა
# #print(len(my_text.split()))
# mylist = my_text.split()
# mylist.append("mariami")
# print(mylist)

# age = 24 
# name = "sandro"
# my_text = "my name is {} and i am {} years old"

# print(my_text.format(name, age))   # format - ახდენს ამ ფიგურული ფრჩხილების იდენტიფიკაციას და ავტომატურად სვავს  მონაცემს


# surname = "samadashvili"
# print(surname.count("a"))   #  count - კონკრეტული მონაცემის რაოდენობის გამოტანა 


# age = 200

# age = str(age)
# print(age.count("0"))




# my_text = "hallo world" 
# print(my_text[7:])
# print(my_text[0:4])
# print(my_text.count("l"))

mytext = "me miyvars mariami"

print(mytext.count("m"))