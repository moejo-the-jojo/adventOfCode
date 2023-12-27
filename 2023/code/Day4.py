import re

data = open("2023\inputs\day4.txt", "r").read()


cards_list = data.split("\n")

sum_of_winnings = 0

for card in cards_list:
    front, back = card.split("|")
    front_numbers = [x for x in front.split(":")[1].split(" ") if x != ""]
    back_numbers = [x for x in back.split(" ") if x != ""]
    right_numbers = set(front_numbers).intersection(set(back_numbers))
    if len(right_numbers) == 0:
        continue
    else:
        sum_of_winnings += 2**(len(right_numbers)-1)

print("Solution part 1: " + str(sum_of_winnings))

original_cards = cards_list.copy()


scratch_counter = 0

index_pattern = re.compile(r"\d+")

for card in cards_list:
    front, back = card.split("|")
    card_id = re.search(index_pattern, card)[0]
    front_numbers = [x for x in front.split(":")[1].split(" ") if x != ""]
    back_numbers = [x for x in back.split(" ") if x != ""]
    right_numbers = set(front_numbers).intersection(set(back_numbers))
    if len(right_numbers) > 0:
        for i in range(1, len(right_numbers)+1):
            cards_list.append(original_cards[int(card_id)+i-1])
    scratch_counter += 1


print("Solution pt 2:" + str(scratch_counter))