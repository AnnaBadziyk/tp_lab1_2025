import random
words = ["ананас", "машина", "кіт", "пальма", "літо", "комп'ютер", "книга", "вікно", "програміст", "сонце"]

word = random.choice(words)
hidden_word = ["_" for _ in word]
attempts_left = 7
guessed_letters = []

print("Вітаємо у грі 'Вгадай слово'!")
print("Загадане слово:", " ".join(hidden_word))
print(f"У вас є {attempts_left} спроб.")

while attempts_left > 0 and "_" in hidden_word:
    letter = input("Введіть літеру: ").lower()

    if not letter.isalpha() or len(letter) != 1:
        print("Введіть одну літеру.")
        continue

    if letter in guessed_letters:
        print("Ви вже вводили цю літеру.")
        continue

    guessed_letters.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                hidden_word[i] = letter
        print("Загадане слово:", " ".join(hidden_word))
    else:
        attempts_left -= 1
        print(f"Немає такої літери. Залишилось спроб: {attempts_left}")
        print("Загадане слово:", " ".join(hidden_word))

# Результат гри
if "_" not in hidden_word:
    print(f"Вітаємо! Ви вгадали слово \"{word}\"!")
else:
    print(f"Гру закінчено. Ви не вгадали слово \"{word}\".")
