
# TIC TAC TOE PROJECT

list1 = [[7, ' | ', 8, ' | ', 9], ['--', '+', '--', '+', '--'], [4, ' | ', 5, ' | ', 6], ['--', '+', '--', '+', '--'], [1, ' | ', 2, ' | ', 3]]


class Board:
    @staticmethod
    def board_show(main_list):
        for mini_list in main_list:
            for value in mini_list:
                print(value, end='')
            print()

    @staticmethod
    def winner_or_not(y):
        if y[0][0] == y[0][2] == y[0][4]:
            print(f'{y[0][0]} won the match')
            return 'won'
        elif y[2][0] == y[2][2] == y[2][4]:
            print(f'{y[2][0]} won the match')
            return 'won'
        elif y[4][0] == y[4][2] == y[4][4]:
            print(f'{y[4][0]} won the match')
            return 'won'
        elif y[0][0] == y[2][2] == y[4][4]:
            print(f'{y[0][0]} won the match')
            return 'won'
        elif y[4][0] == y[2][2] == y[0][4]:
            print(f'{y[4][0]} won the match')
            return 'won'
        elif y[0][0] == y[2][0] == y[4][0]:
            print(f'{y[0][0]} won the match')
            return 'won'
        elif y[0][2] == y[2][2] == y[4][2]:
            print(f'{y[0][2]} won the match')
            return 'won'
        elif y[0][4] == y[2][4] == y[4][4]:
            print(f'{y[0][4]} won the match')
            return 'won'


Board.board_show(list1)
list2 = []
Number_count = 0
while Number_count < 9:
    while Number_count < 9:
        p = int(input("It's your turn 'x' move to which place--\n"))
        if p not in list2:
            list2.append(p)
            count1 = 0
            for i in list1:
                count2 = 0
                for j in i:
                    if j == p:
                        list1[count1][count2] = 'X'
                        Number_count += 1
                    count2 += 1
                count1 += 1
            break
        else:
            print("--Already filled by some one--")
            continue
    Board.board_show(list1)
    z = Board.winner_or_not(list1)
    if z == 'won':
        print('GAME OVER!!!!!')
        break
    while Number_count < 9:
        o = int(input("It's your turn 'o' move to which place--\n"))
        if o not in list2:
            list2.append(o)
            count1 = 0
            for i in list1:
                count2 = 0
                for j in i:
                    if j == o:
                        list1[count1][count2] = 'O'
                        Number_count += 1
                    count2 += 1
                count1 += 1
            break
        else:
            print("--Already filled by some one--")
            continue
    if Number_count < 9:
        Board.board_show(list1)
        result = Board.winner_or_not(list1)
    else:
        print("Maximum ATTEMPTS EXCEED!!!!!!")
    if result == 'won':
        print('GAME OVER!!!!!')
        break