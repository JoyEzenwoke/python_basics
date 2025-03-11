my_sentence ="python is fun and powerful!"
print(len(my_sentence))
print(my_sentence[0])
print(my_sentence[10:])
print(my_sentence.lower())
print(my_sentence.count('o'))
print(my_sentence.find('fun'))
print(my_sentence.replace('powerful','amazing'))
new_message = "learning python is exciting!"
print(my_sentence + " " + new_message)
print("{} {}".format(my_sentence, new_message))
print(f"{my_sentence} {new_message}")
print(dir(my_sentence))
help(str.replace)
