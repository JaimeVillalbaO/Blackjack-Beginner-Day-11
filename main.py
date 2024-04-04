import random
from acsi_day11 import logo
import os

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

credits_init = 100
result = ''
start_game= 'y'
result = None

def money (result_money, credits_init_money, bet_money_money):
    if result_money == 2:
        return (credits_init + bet_money)
    elif result_money == 1:
        return(credits_init)
    elif result_money == 0:
        return(credits_init  - bet_money)
    

while start_game == 'y': 


    start_game = input('\nDo you want to play a game of blackjack? Type "y" or "n": ').lower()
    os.system('cls') 
    print(logo)
    
    try_bet = True
    while try_bet : 
        print(f'Your current credits are ${credits_init}')
        bet_money = int(input('How much do you want to bet? 5, 10, 20 or 50 ? '))
        

        if bet_money > credits_init: 
            print('Your bet amount is greater than you credits. Try again')
            try_bet = True
        else: try_bet = False

    user_cards = []
    computer_cards = []
    if start_game == 'y':
        user_cards.append(random.choice(cards))
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        suma_user_cards = sum(user_cards)
        print(f'\nYour cards are {user_cards}. Current score: {suma_user_cards}')
        print(f'Computer\'s first cards is {computer_cards}.\n')


        hit_option = 'y'
        while hit_option == 'y':
            if suma_user_cards == 21 :
                result = 2
                print('BLACKJACK !!!  You win !!!')
                hit_option = 'game over'
                break
            hit_option = (input('Type \'y\' to get another card, type \'n\' to pass: '))
            if hit_option == 'n':
                continue
            
            user_cards.append(random.choice(cards))
            suma_user_cards = sum(user_cards)
            
            if suma_user_cards > 21 and user_cards[-1] == 11 :
                user_cards[-1] = 1
                suma_user_cards = sum(user_cards)
            
            if suma_user_cards > 21 : 
                computer_cards.append(random.choice(cards))
                suma_computer_cards = sum(computer_cards)
                print(f'\nYour final hand is {user_cards}. Score: {suma_user_cards}')
                print(f'Computer\'s final hand is {computer_cards}. Sscore: {suma_computer_cards}\n')
                result = 0
                print('You went over. You lose 😭')
                break      
            
            print(f'\nYour cards are {user_cards}. Current score: {suma_user_cards}')
            print(f'Computer\'s first cards is {computer_cards}.\n')
            if suma_user_cards == 21 :
                result = 2
                print('BLACKJACK !!!  You win  !!!')
                hit_option = 'game over'
                break
             
        def hit_over():     
        
            computer_cards.append(random.choice(cards))
            suma_computer_cards = sum(computer_cards)
            while suma_computer_cards < 17 :
                computer_cards.append(random.choice(cards))                
                suma_computer_cards = sum(computer_cards)
                if suma_computer_cards > 21 and 11 in computer_cards:
                    computer_cards.remove(11)
                    computer_cards.append(1)
            print(f'\nYour final hand is {user_cards}. Score: {suma_user_cards}')
            print(f'Computer\'s final hand is {computer_cards}. Score: {suma_computer_cards}\n')    
            if suma_computer_cards > suma_user_cards and suma_computer_cards < 21 :
                
                print('You went over. You lose 😭')
                return 0
            elif suma_computer_cards == 21:
                
                print('Blackjack from computer !!! You went over. You lose 😭')
                return 0
            elif suma_computer_cards == suma_user_cards:
                
                print('It is a draw  !!!')       
                return 1            
            else: 
                
                print('you winnnnnnnn  !!!!')
                return 2
        

        if hit_option == 'n':
            result = hit_over()
  
     
    credits_final = money(result_money=result, credits_init_money=credits_init, bet_money_money=bet_money)

    if credits_final <= 0: 
        print(f'You have ${credits_final} credits. Game Over')
        break
    else :
        print(f'You have ${credits_final} credits. ')
    credits_init = credits_final

    