import sys, re

if len(sys.argv) < 2:
    print('python3 sol.py <input file>')
    exit(1)

input = open(sys.argv[1], 'r').read()
lines = input.split('\n')
total = 0

def hand_type(hand):
    card_ranking = 'J23456789TQKA'
    rankings = [card_ranking.index(c) * pow(10, 10 - (i*2)) for i, c in enumerate(hand)]
    bias = sum(rankings)

    counts = {}
    for h in hand:
        if h == 'J':
            continue
        if h not in counts:
            counts[h] = 0
        counts[h] += 1

    
    count_ns = sorted(counts.values(), reverse=True)
    if hand == 'JJJJJ':
        return 700000000000000
    for h in hand:
        if h == 'J':
            count_ns[0] += 1

    if count_ns[0] == 5: return 700000000000000 + bias
    elif count_ns[0] == 4: return 600000000000000 + bias
    elif count_ns[0] == 3 and count_ns[1] == 2: return 500000000000000 + bias
    elif count_ns[0] == 3: return 400000000000000 + bias
    elif count_ns[0] == 2 and count_ns[1] == 2: return 300000000000000 + bias
    elif count_ns[0] == 2: return 200000000000000 + bias
    elif count_ns == [1, 1, 1, 1, 1]: return 100000000000000 + bias

hand_bids = []

for l in lines:
    hand, bid = l.split()
    bid = int(bid)
    # hand = ''.join(sorted([h for h in hand]))
    hand_bids += [(hand, bid, hand_type(hand))]

hand_bids = sorted(hand_bids, key=lambda x: x[2])
for i, hb in enumerate(hand_bids):
    total += (i + 1) * hb[1]

[print(i) for i in hand_bids]

file_name = sys.argv[1].replace(".txt", "")
file_padding = " " * (10 - len(file_name))
print(f'{file_name}{file_padding}{total}')