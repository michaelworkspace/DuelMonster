"""
#* A Text Base Monster Duel Game Written in Python
#* @author Michael Le
#* @youtube michaelworkspace
#* @version python 3.7.3
"""

from random import randint
import time

hero_name = input("What brave soul is this?")
monster = {"min_attack": 5, "max_attack": 20}


def begin_game():

    player_health = 50
    monster_health = 50
    game_running = True

    while game_running:
        print("Player Choices:")
        print("1) Attack")
        print("2) Heal")
        print("3) Run")
        print("4) Quit")
        print("--------------------" * 5)

        try:
            hero_choice = int(input("What do you want to do?"))
        except ValueError:
            print("WARNING: That is not a valid choice. Choose again.\n")
            continue
        time.sleep(1)

        #! Attack
        if hero_choice == 1:
            player_attack_damage = randint(5, 15)
            print(f"{hero_name} attack for {player_attack_damage} damage.\n")
            monster_health -= player_attack_damage
            if monster_health <= 0:
                monster_health = 0
                game_running = False
                print(
                    f"Monster's health is now {monster_health}. {hero_name} defeated the monster. {hero_name} wins!\n")
            else:
                print(f"Monster's health is now at {monster_health}.\n")
                damage = randint(monster["min_attack"], monster["max_attack"])
                player_health -= damage
                print(f"Monster attack {hero_name} back for {damage}.")
                if player_health <= 0:
                    player_health = 0
                    print(
                        f"{hero_name} have {player_health} HP now. Monster Won!\n")
                    game_running = False
                    time.sleep(1)
                else:
                    print(f"{hero_name} have {player_health} now HP.\n")
                    time.sleep(1)

        #! Heal
        elif hero_choice == 2:
            heal = randint(5, 10)
            player_health += heal
            print(
                f"{hero_name} uses a healing potion. Gained {heal} health. {hero_name} now has {player_health} HP.")
            damage = randint(monster["min_attack"], monster["max_attack"])
            player_health -= damage
            print(f"Monster attack {hero_name} back for {damage}.")
            if player_health <= 0:
                player_health = 0
                print(
                    f"{hero_choice} have {player_health} HP now. Monster Won!\n")
                game_running = False
                time.sleep(1)
            else:
                print(f"{hero_name} have {player_health} now HP.\n")
                time.sleep(1)

        #! Run
        elif hero_choice == 3:
            print("LOL! Uh.... Running is NOT AN OPTION. Pick again")

        #! Quit
        elif hero_choice == 4:
            print(f"Thanks for playing. Good day {hero_name}!\n")
            game_running = False


if __name__ == '__main__':
    begin_game()
