questions = "Какой сегодня месяц?"
right_answer = "июнь"

print(questions)
user_answer = input()
attempts = 1
lives=3

while user_answer != right_answer and lives > 0:
    lives -= 1
    print("Wrong try again", attempts)
    user_answer = input()
    attempts += 1

if user_answer == right_answer:
    print("Well done")
    print("Attempts", attempts)
else:
    print("Too bad.")
#Посчитать количество попыток в конце
questions = "Где вы сейчас?"