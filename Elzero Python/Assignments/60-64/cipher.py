cipher_char = ['X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W']
cipher = "KZCK ULDS JEZWW JKRZIJ"
decoded_cipher = ""
# for char in cipher:
    # if char == "U":
    #     decoded_cipher += "X"
    # elif char == "V":
    #     decoded_cipher += "Y"
    # elif char == "W":
    #     decoded_cipher += "Z"
    # else:
    #     decoded_cipher += cipher_char[cipher_char.index(char) - 3]
# print(decoded_cipher)
# one_word = ""
# for word in cipher:
#     for char in word:
#         if char == "U":
#             one_word += "X"
#         elif char == "V":
#             one_word += "Y"
#         elif char == "W":
#             one_word += "Z"
#         else:
#             one_word += cipher_char[cipher_char.index(char) + 3]
#     print(one_word)
#     decoded_cipher.append(word)
#     word = ""
# print(decoded_cipher)
cipher_decryption = {
    "X": "A",
    "Y": "B",
    "Z": "C",
    "A": "D",
    "B": "E",
    "C": "F",
    "D": "G",
    "E": "H",
    "F": "I",
    "G": "J",
    "H": "K",
    "I": "L",
    "J": "M",
    "K": "N",
    "L": "O",
    "M": "P",
    "N": "Q",
    "O": "R",
    "P": "S",
    "Q": "T",
    "R": "U",
    "S": "V",
    "T": "W",
    "U": "X",
    "V": "Y",
    "W": "Z",
    " ": " "
}
for char in cipher:
    decoded_cipher += cipher_decryption[char]
print(decoded_cipher)