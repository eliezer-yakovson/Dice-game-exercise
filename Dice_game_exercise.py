import random

def roll_two_d6() -> tuple[int, int]:
    r1 = random.randint(1,6)
    r2 = random.randint(1,6)
    return (r1,r2)

def is_bust(score: int) -> bool:
    if score > 100:
        return True
    return False

def is_exact_100(score: int) -> bool:
    if score == 100:
        return True
    return False

def closer_to_target(a: int, b: int, target: int = 100) -> int | None:
    if target - a > target - b:
        return 2
    elif target - a < target - b:
        return 1
    return None

def tie_breaker() -> int:
    while True:
        roll_two1 = roll_two_d6()
        roll_two2 = roll_two_d6()
        closer = closer_to_target(sum(roll_two1),sum(roll_two2))
        if closer == 1:
            return 1
        if closer == 2:
            return 2

def turn_decision(input_fn) -> str:
    if input_fn:
        return input_fn
    while True:
        i = input()
        if i == "r" or i == "p":
            return i
        print("enter only r or p")


def play_game():
    sum_1 = sum_2 = 0
    tor = True
    Number_transfer_turns = 0
    while True:
        if tor:    
            print("תור שחקן - 1" ,end = " ")
            print("הניקוד שלך הוא ",sum_1 ,end = " ")
            print("הניקוד של שחקן 2 הוא ", sum_2)
            print("בחר r=להטיל / p=להעביר")
            player1 = turn_decision(input())
            if player1 == "r":
                roll_two = roll_two_d6()
                print("התוצאות ",roll_two, end=" ")
                sum_1 += sum(roll_two)
                print("ניקודך כעת הוא ",sum_1 )
                if is_bust(sum_1):
                    print("שחקן 2 ניצח")
                    return
                if is_exact_100(sum_1):
                    print("שחקן 1 ניצח")
                    return
                Number_transfer_turns = 0
            else:
                Number_transfer_turns += 1
                if Number_transfer_turns == 2:
                    if sum_1 < sum_2:
                        print("המנצח הוא ",sum_1)
                        return
                    if sum_1 < sum_2:
                        print("המנצח הוא ",sum_2)
                        return
                    else:
                        w = tie_breaker()
                        print("המנצח הוא ",w)
                        return           
        else:
           print("תור שחקן - 2" ,end = " ")
           print("הניקוד שלך הוא ",sum_2,end = " " )
           print("הניקוד של שחקן 1 הוא ", sum_1)
           print("בחר r=להטיל / p=להעביר")
           player2 = turn_decision(input())
           if player2 == "r":
               roll_two = roll_two_d6()
               print("התוצאות ",roll_two, end=" ")
               sum_2 += sum(roll_two)
               print("ניקודך כעת הוא ",sum_2 )
               if is_bust(sum_2):
                   print("שחקן 1 ניצח")
                   return
               if is_exact_100(sum_2):
                   print("שחקן 2 ניצח")
                   return
               Number_transfer_turns = 0
           else:
               Number_transfer_turns += 1
               if Number_transfer_turns == 2:
                   if sum_1 < sum_2:
                       print("המנצח הוא ","1")
                       return
                   if sum_1 < sum_2:
                       print("המנצח הוא ","2")
                       return
                   else:
                       w = tie_breaker()
                       print("המנצח הוא ",w)
                       return  
        tor = not tor

    

if __name__ == "__main__":
   a= play_game()

