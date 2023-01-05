def print_board(xstate,ystate):
    zero = 'X' if xstate[0] else ('O' if ystate[0] else 0)
    one = 'X' if xstate[1] else ('O' if ystate[1] else 1)
    two = 'X' if xstate[2] else ('O' if ystate[2] else 2)
    three = 'X' if xstate[3] else ('O' if ystate[3] else 3)
    four = 'X' if xstate[4] else ('O' if ystate[4] else 4)
    five = 'X' if xstate[5] else ('O' if ystate[5] else 5)
    Six = 'X' if xstate[6] else ('O' if ystate[6] else 6)
    Seven = 'X' if xstate[7] else ('O' if ystate[7] else 7)
    Eight = 'X' if xstate[8] else ('O' if ystate[8] else 8)

    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{Six} | {Seven} | {Eight}")


def check_win(lst):
    checkwin = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in checkwin:
        if lst[i[0]]+lst[i[1]]+lst[i[2]]==3:
            return True
    False
def tic_tac_toe():
    xstate = [0,0,0,0,0,0,0,0,0]
    ystate = [0,0,0,0,0,0,0,0,0]
    print_board(xstate , ystate)

    turn =1 # 1 for X and 0 for O
    while(True):
        

        if check_win(xstate):
            return ("X is the winner!")
        if check_win(ystate):
            return ("O is the winner!")
        if turn==len(xstate):
            return ("It's a draw!")
        if turn%2==1:
            print("X's turn ")
            value = int(input("Enter a value: "))
            # board is number from 0 to 5 please enter the postion
            xstate[value] = 1
            turn =turn+1
            print_board(xstate , ystate)

        else:
            print("Y's turn")
            value = int(input("Enter the value: "))
            ystate[value] =1
            turn=turn+1
            print_board(xstate , ystate)
        


print(tic_tac_toe())
