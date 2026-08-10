def caesar(text, shift, choice):
    result = ""

    if choice == "d":
        shift = -shift

    for ch in text:
        if ch.isalpha():  ##number or special character will not be changed
            if ch.islower():
                result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a')) ## order of the character is changed to a number and then shifted and then converted back to character
            else:
                result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A')) ## order of the character is changed to a number and then shifted and then converted back to character
        else:
            result += ch

    return result


text = input("Enter text: ")
shift = int(input("Enter shift value: "))
choice = input("Encrypt or Decrypt (e/d): ")

print("Result:", caesar(text, shift, choice))