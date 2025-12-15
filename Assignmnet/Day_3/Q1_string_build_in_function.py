str1="sadanand SHARANBASAPPA "
str2="MHETRE"

str3=str1.capitalize() # capitalize() = 1st letter is become capital reamaning will be small
print(str3)
str3=str2.capitalize()
print(str3)

print("\n")
print(str1.swapcase()) # swapcase() = conert small letter to capital && capital to small letter
print(str2.swapcase())

print("\n")
print(str1.title()) # title() = 1st letter of each word is capital
print(str2.title())

print()
num1="12345"
num2="12x34"
print(num1.isnumeric()) # isnumeric() = if string containt only numbers then become True
print(num2.isnumeric()) # isnumeric() = if string does not containt only numbers then become False

print()
print(str1.isupper()) # isupper() = it check string containt only  upper case (false)
print(str2.isupper()) # isupper() = it check string containt only  upper case (true)

print()
str3="sanket"
print(str1.islower()) # islower() = it check string containt only  lower case (false)
print(str3.islower()) # islower() = it check string containt only  lower case (true)

print()
txt = "sadanand"
x = txt.count("a")
y = txt.count("n") # count() = method returns the number of times a specified value appears in the string.
print(x)
print(y)




