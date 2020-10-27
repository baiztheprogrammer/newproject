import random
file1 = open('players.txt','w')
for i in range(6):
    player = input('type player username: ')
    file1.write(player+'\n')
file1.close()
file2 = open('players.txt')
players_list = file2.readlines()
cards = []
for i in range(6):
    cost = random.randint(2,11) + random.randint(2,11)
    check = input(f"your hand: {cost} need another card? yes or no: ")
    if check == 'yes':
        cost = cost + random.randint(2,11)
    elif check == 'no':
        cost = cost
    else:
        print('answer correctly, yes or no')
    cards.append(cost)
print(cards)
i = 0
while i < len(cards):
    if cards[i] > 21:
        cards[i] = 0
    i = i + 1
max_cost = max(cards)
max_index = cards.index(max_cost)
winner = players_list[max_index]
print(f'winner! : {winner}')