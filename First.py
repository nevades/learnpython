# print function, open and close parenthesis = (), String = ""
# code gets executed in order (Top to Bottom)
print("Hello Friend")

# three types of data : String, Numbers, Boolean
# character_name is an example of a variable
# use _ when using 2 words in a variable (use character_name, not charactername or character name)
character_name = "John"
character_age = 30
is_male = False

# you can use ,, or ++ to concatenate
print("Hello World")
print("There was once a man called " + character_name + ", ")

# you cant concatenate strings with numbers
# so convert it to the same data type
print("he was", str(character_age), "years old")

print("he really likes the name george")
print("he didn't like being 70")

# create a new line
print("Hello\nBoi")

# you cant just print a quotation. use backslash to render to literally
print("hi\"hi")

# you can print variables
phrase = "Python"
print(phrase)

# or a slash
print("hi\\hi")

# concatenation
print(phrase + " is cool")

# some common functions
# .lower function will convert all the string to lower case
print(phrase.lower())
# .upper will convert all string to upper case
print(phrase.upper())
# check to see if the string is entirely upper case or lower case
# will give a true or false value
print(phrase.islower())
print(phrase.isupper())
# clarification
phrase2 = "HELLO"
print(phrase2.isupper())

# you can use functions in combination with each other
# first it will convert to upper then check is the string is all upper case
phrase3 = "hello world"
print(phrase3.upper().isupper())

# len(string) will check the amount of characters in the string, it will count spaces as well
example = "hello Friend"
print(len(example))

# you can grab individual characters from a string, the index starts with ZERO
print(example[0])
