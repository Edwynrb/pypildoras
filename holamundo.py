age = 40

name = "edwyn"
 
print (id(age))

# boolean data
is_mayor_age= True
is_sunday = False
print (int(is_sunday))

# float data
first_value = 0.7
second_value = 0.6
print(first_value + second_value)

# strings
name_one = "edwyn"
name_two = "eduin"
text = """ this is a text for prove code
in this situation I work in the enterprise of ice
good code

"""
print(name_one, name_two, text)
print(len(name_one))

# prefix and subfix
# problem in this case i need remove prefix the variable product_one and subfix of variable product_two 
product_one = "0001 - apple"
product_two = "apple - 0001"
print(product_one.removeprefix("0001 - "))
print(product_two.removesuffix("- 0001"))

# indexing and slicing 
# problem in this case print first letter of the string Hi, world with indexing
String = "Hi, world"
print(String[1])
# problem I need extract last character of the string 
print(String[-1])