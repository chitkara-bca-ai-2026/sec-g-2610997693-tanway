sentence = input("Enter a sentence: ")

total_chars = len(sentence)
words_count = len(sentence.split())

vowels = "aeiouAEIOU"
vowels_count = 0
consonants_count = 0
digits_count = 0
spaces_count = 0
special_count = 0

for char in sentence:
    if char in vowels:
        vowels_count += 1
    elif char.isalpha():
        consonants_count += 1
    elif char.isdigit():
        digits_count += 1
    elif char.isspace():
        spaces_count += 1
    else:
        special_count += 1

total_letters = vowels_count + consonants_count
vowel_percentage = (vowels_count / total_letters * 100.0) if total_letters > 0 else 0.0

print("=" * 50)
print("DOCUMENT ANALYSIS REPORT")
print("=" * 50)
print(f"Sentence: {sentence}")
print(f"Total characters: {total_chars}")

print()
print("--- Character Breakdown ---")
print(f"{'Words:':<18}{words_count}")
print(f"{'Vowels:':<18}{vowels_count}")
print(f"{'Consonants:':<18}{consonants_count}")
print(f"{'Digits:':<18}{digits_count}")
print(f"{'Spaces:':<18}{spaces_count}")
print(f"Special characters: {special_count}")

print()
print("--- Summary ---")
print(f"Total letters: {total_letters}")
print(f"Vowel percentage: {vowel_percentage:.1f}%")

print()
print("=" * 50)
print("Analysis Complete!")
print("=" * 50)
