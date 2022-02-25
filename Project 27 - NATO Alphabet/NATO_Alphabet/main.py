import pandas

alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}

word = input("Enter a word: ").upper()

result = [alphabet_dict[letter] for letter in word]

print(result)

