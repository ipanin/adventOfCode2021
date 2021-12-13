# Day 4: Giant squid bingo
import util

def test(fname, expected1, expected2):
    with open(util.full_name(fname)) as f:
        line = f.readline().rstrip('\n')
        draw_numbers = [int(item) for item in line.split(',')]
        blocks = f.read().strip().split('\n\n')
    print("Loaded", fname)
    cards = []
    for block in blocks:
        card = []
        for row in block.split('\n'):
            nums = [int(n) for n in row.split()]
            card.append(nums)
        cards.append(card)

    cards1 = [[row.copy() for row in card] for card in cards]
    result = solve1(draw_numbers, cards1)
    print("Part 1.", result)
    util.assert_equal(result, expected1)

    result = solve2(draw_numbers, cards)
    print("Part 2.", result)
    util.assert_equal(result, expected2)

# calc first win card score
def solve1(numbers, cards):
    for n in numbers:
        for card in cards:
            if mark(card, n):
                return score(card, n)

# calc last win card score
def solve2(numbers, cards):
    not_won = [i for i in range(len(cards))]
    for n in numbers:
        not_won2 = not_won.copy()
        for i in not_won:
            if mark(cards[i], n):
                not_won2.remove(i)
                if len(not_won2) == 0:
                    return score(cards[i], n)
        not_won = not_won2

def mark(card, n: int):
    for r, row in enumerate(card):
        for c, v in enumerate(row):
            if v == n:
                card[r][c] = -1
                if all(x==-1 for x in row) or all(card[i][c]==-1 for i in range(len(card))):
                    return True
    return False

def score(card, n: int):
    res = 0
    for row in card:
        res += sum(c for c in row if c != -1)
    return res * n 

test("input_sample.txt", 4512, 1924)
test("input.txt", 11774, 0)