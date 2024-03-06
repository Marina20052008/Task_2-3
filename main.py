ter = "The reasonable man adapts himself to the world; the unreasonable one persists in trying to adapt the world to himself."
# Розділяємо наше речення на слова
words = ter.split()
# Знаходимо потрібне слово в реченні.
index_1 = words.index("reasonable")
index_2 = words.index("unreasonable")
# Міняємо містями.
words[index_1], words[index_2] = words[index_2], words[index_1]
# Розділені раніше слова ми знову перетворюємо в повноцінне речення.
swapped_ter = ' '.join(words)

print(swapped_ter)