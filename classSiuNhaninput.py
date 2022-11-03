import random
class Player ():
    def __init__(self,name,HP):
        self.name = name
        self.HP = int(HP)
    def __str__(self):
        return  f"Nhan vat la {self.name} , co {self.HP} mau"
a = input("nhap vao ten nhan vat :")
b = input("luong mau la :")
c = input("nhap vao ten nhan vat :")
d = input(" nhap vao luong mau :")

class Weapon():
    def __init__(self):
        self.weapon = random.choice(['dao','kiem'])
        self.damge = random.choice([20,30])
    def __str__(self):
        return "anh ay dung vu khi {}, co damge la {}".format(self.weapon,self.damge)
def slove(player1,player2):

    player1_weapon = Weapon()
    player2_weapon = Weapon()
    print(player1.__str__(), player1_weapon)
    print(player2.__str__(), player2_weapon)
    round_num = 0
    play1_turn = random.randrange(10)
    play2_turn = random.randrange(10)
    if play1_turn > play2_turn:
        print("Player 1 hit Player 2")

        while player1.HP > 0 and player2.HP > 0 :
            round_num+=1
            player2.HP = player2.HP - player1_weapon.damge
            if player2.HP <= 0 :
                result = ('player1',player1)
                break
            player1.HP = player1.HP - player2_weapon.damge
            if player1.HP <=0 :
                result = ('player2', player2)
                break
            print("player_1 con lai: {}".format(player1.HP))
            print("player_2 con lai: {}".format(player2.HP))
    else:
        print("player 2 hit Player 1")

        while player1.HP > 0 and player2.HP > 0:
            round_num +=1
            player1.HP = player1.HP - player2_weapon.damge
            if player1.HP <= 0:
                result = ('player2',player2)
                break
            player2.HP = player2.HP - player1_weapon.damge
            if player2.HP <= 0:
                result = ('player1',player1)
                break
            print("player_1 con lai: {}".format(player1.HP))
            print("player_2 con lai: {}".format(player2.HP))
    print("Ng thang cuoc la : {}, con lai {} mau ".format(result[0],result[1]))
    return result
def main():
    player1 = Player(a,b)
    player2 = Player(c,d)
    print(slove(player1, player2))
if __name__ == "__main__":
    main()

