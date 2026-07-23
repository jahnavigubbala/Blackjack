from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_pick = random.choices(cards, k=2)
comp_pick = random.choices(cards, k=1)
sum_user = 0
sum_comp = 0
for int_u in user_pick:
    sum_user += int_u
bust = True
print(f"Your cards: {user_pick}, current score is {sum_user}")
print(f"Computer's first card: {comp_pick} ")
if 11 in user_pick and 10 in user_pick:
    print("BlackJack! You win!")
    bust = False
while bust:
    to_hit = input("Would you like to hit (get another card)? Type yes or no: ").lower()
    if to_hit == "yes":
        user_pick += random.choices(cards, k=1)
        sum_user += user_pick[-1]
        print(f"Your cards: {user_pick}, current score is {sum_user}")
        print(f"Computer's first card: {comp_pick} ")
        if sum_user > 21:
            print(f"Bust! Your hand is: {user_pick}, final score is {sum_user}")
            print(f"Computer's first card: {comp_pick} ")
            bust = False
            break
    elif to_hit == "no":
        user_pick = user_pick
        sum_user = sum_user
        print(f"Your cards: {user_pick}, current score is {sum_user}")
        comp_pick += random.choices(cards, k=1)
        for ints in comp_pick:
            sum_comp += ints
        while sum_comp < 17:
            comp_pick += random.choices(cards, k=1)
            sum_comp += comp_pick[-1]
            if sum_comp > 21:
                print("Comuter's hand is bust!")
                print(f"Your final hand is {user_pick}, final score is {sum_user}")
                print(f"Computer's final hand is {comp_pick}, final score is {sum_comp}")
                bust = False
        if sum_comp < 22:
            if sum_user > sum_comp:
                print("You win!")
            elif sum_user == sum_comp:
                print("Draw")
            elif sum_user < sum_comp and sum_comp > 21:
                print("computer's hand is bust!")
                bust = False
            else:
                print("You lose!")
                if 11 in comp_pick and 10 in comp_pick and len(comp_pick) == 2:
                    print("Computer has a BlackJack!")
            print(f"Your final hand is {user_pick}, final score is {sum_user}")
            print(f"Computer's final hand is {comp_pick}, final score is {sum_comp}")
            bust = False
    else:
        print("Invalid input")
