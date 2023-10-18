def remove_vowels(word):
    vowels = "aeiouAEIOU"
    result = ""
    for letter in word:
        if letter not in vowels:
            result += letter
    return result

user_input = input("Istalgan gapni kiriting: ")
modified_input = remove_vowels(user_input)
print("Natija:", modified_input)