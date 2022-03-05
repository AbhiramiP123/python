main_strings=input("Type a string:")
char=main_strings[0]
main_strings=main_strings.replace(char,'$')
print(char+main_strings[1:])
