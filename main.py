str = input("Enter your string ==> ")
str1 = str[::-1]
if str[::-1] == str1:
     print(f"{str} is palindrome")

str = input("Enter your string ==> ")
list = []
len = len(str)
count_elements = 0
count = int(input("Enter count of words in list --> "))
for i in range(count):
    word_to_upper = input("Enter word tp upper --> ")
    list.append(word_to_upper)
    str1 = str.replace(list[i], word_to_upper.upper())
else:
    print(str1)

str = input("Enter your text -->\n")
count = str.count(".") + str.count("!") + str.count("?")
print(f"Count of strings in your text is {count}")
