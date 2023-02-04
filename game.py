import threading
from random import randint

score = 0
game_over = False

def user_answer():
    global score
    num_1 = randint(1, 9)
    num_2 = randint(1, 9)
    answer = int(input(f"{num_1} + {num_2} = "))
    if answer == num_1 + num_2:
        print("Right!")
        score += 1
    else:
        print("Wrong!")

def time_is_up():
    global game_over
    print("\nTime is up!")
    game_over = True

for i in range(3):
    answer_thread = threading.Thread(target=user_answer, daemon=True)
    timer_thread = threading.Timer(3, time_is_up)

    answer_thread.start()
    timer_thread.start()

    answer_thread.join(4)
    if game_over:
        break
    timer_thread.cancel()


print(f"{score=}")