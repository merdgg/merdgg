import time
import random


print("всё с маленькой буквы")
comp_score = 0 
your_score = 0

rounds = int(input("сколько раундов сыграем?  "))
print()

while True:
    if rounds <= 0:
        print("раунды закончились!")
        break
    player = input("камень, ножницы или бумага? ")

    if player == "камень":
        print("вы выбрали камень")
    elif player.lower() == "ножницы":
        print("Вы выбрали ножницы")
    elif player.lower() == "бумага":
        print("Вы выбрали бумагу")
    else:
        print("нет такой команды")
        break

    print("игрок 2 выбирает камень, ножницы или бумага..")
    time.sleep(3)

    computer = random.randint(1,3)

    if computer == 1:
        computer = "камень"
    elif computer == 2:
        computer = "ножницы"
    elif computer == 3:
        computer = "бумага"

    print("игрок 2 сделал решение!")
    time.sleep(1)
    print()
    print("камень,ножницы бумага!")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("3!")
    time.sleep(0.5)
    
    if player == computer:
        print("ничья! игрок 2:", computer, "игрок 1:", player)
    elif player == "ножницы" and computer == "бумага" or player == "камень" and computer == "ножницы" or player == "бумага" and computer == "камень":
        print("победа! игрок 2:", computer, "игрок 1:", player)
        your_score +=1
    else:
        print("проигрыш! игрок 2:", computer, ", игрок 1:", player)
        comp_score +=1
    
    rounds -=1
print("игра окончена")
print("игрок1:",your_score)
print("игрок2:",comp_score)
if comp_score < your_score:
    print("поздравляю! игрок  выиграл")
else:
    print("вы проиграли! попробуйте ещё раз:(")
