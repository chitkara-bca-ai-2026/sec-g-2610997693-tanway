print("=" * 50)
print("               TEXT PROCESSING TOOL")
print("=" * 50)
sentence = input("Enter a sentence: ")

print()
print("--- Processing Results ---")
pos = int(input("Enter position for indexing: "))
print(f"Character at position {pos}  : '{sentence[pos]}'")

start = int(input("Enter start index for slicing : "))
end = int(input("Enter end index for slicing   : "))
print(f"Sliced string [{start}:{end}]      : '{sentence[start:end]}'")

print(f"Uppercase                : {sentence.upper()}")
print(f"Lowercase                : {sentence.lower()}")

word_to_replace = input("Enter word to replace    : ")
replacement_word = input("Enter replacement word   : ")
replaced = sentence.replace(word_to_replace, replacement_word)
print(f"After replace            : {replaced}")
print(f"Length of sentence       : {len(sentence)}")

print()
print("=" * 50)
print("Analysis Complete!")
print("=" * 50)
