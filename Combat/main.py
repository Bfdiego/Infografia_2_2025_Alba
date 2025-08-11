import random
from character import Character

rogue = Character(100, 10, 0.1, 0.4)
tank = Character(500, 8, 0.3, 0.2)
wizard = Character(80, 5, 0.1, 0.8)
paladin = Character(400, 6, 0.4, 0.05)

characters = [rogue, tank, wizard, paladin]
characters_chosen = []
character_labels = ["Rogue", "Tank", "Wizard", "Paladin"]
n_players = 0
while True:
    n_players = int(input("Ingrese numero de jugadores (2-4): "))
    if n_players in [2, 3, 4]:
        break
    print("Numero invalido, intente de nuevo.")
for i in range(n_players):
    input(f"Jugador {i+1}, presione Enter para elegir personaje...")
    for j, character in enumerate(characters):
        print(f"{j+1}: {character_labels[j]}")

    choice = int(input("Ingrese el numero del personaje: ")) - 1
    chosen_character = characters.pop(choice)
    character_labels.pop(choice)
    name = input("Ingrese el nombre de su personaje: ")
    chosen_character.set_name(name)
    characters_chosen.append(chosen_character)

n_turns = int(input("Ingrese numero de turnos: "))

for turn in range(n_turns):
        
    for n_player in range(n_players):
        player = characters_chosen[random.randint(0, n_players - 1)]
        print(f"Turno {turn + 1}: {player.name} ataca")
        input("Presione Enter para elegir victima...")
        for j, character in enumerate(characters_chosen):
            print(f"{j + 1}: {character.name}")
        victim_choice = int(input("Ingrese el numero de la victima: ")) - 1
        victim = characters_chosen[victim_choice]
        player.attack(victim)

winner = max(characters_chosen, key=lambda c: c.hp)
print(f"El ganador es {winner.name} con {winner.hp} hp restante.")

