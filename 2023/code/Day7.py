from collections import defaultdict

data = open("2023\inputs\day7.txt", "r").read()

all_cards = data.split("\n")

all_cards_split = [x.split(" ") for x in all_cards]

total = 0

valued_cards = all_cards_split.copy()

for index, card in enumerate(all_cards_split):
    curr_number = "0"
    card_dict = defaultdict(lambda: 0)
    values = list(card[0])
    for single in values:
        card_dict[single] += 1
    match sorted(card_dict.values()):
        case [5]:
            curr_number = "7"
        case [1,4]:
            curr_number = "6"
        case [2,3]:
            curr_number = "5"
        case [1,1,3]:
            curr_number = "4"
        case [1,2,2]:
            curr_number = "3"
        case [1,1,1,2]:
            curr_number = "2"
        case _:
            curr_number = "1"
    for highest_card in values:
        match highest_card:
            case "A":
                curr_number += "14"
            case "K":
                curr_number += "13"
            case "Q":
                curr_number += "12"
            case "J":
                curr_number += "11"
            case "T":
                curr_number += "10"
            case _:
                curr_number += "0" + str(highest_card)
    valued_cards[index].append(curr_number)

valued_cards.sort(key=lambda x: x[2])

for index, score in enumerate(valued_cards):
    total += int(score[1]) * (index+1)

print("Solution pt 1:", total)