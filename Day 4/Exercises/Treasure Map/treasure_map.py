row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ") - input sempre vem em str ent tem q transformar sempre

horizontal = int(position[0]) - o que for na posição 0, é o primeiro dígito do input, vai no horizontal, lembra de converter os bagulho

vertical = int(position[1]) - O que for na posição 1, é o segundo dígito do input, vai no vertical, lembra de converter os bagulho

map[vertical -1][horizontal -1] = "X" - pega a posição inserida 1 e a 2 -1 pra cada e altera o valor delas para X

print(f"{row1}\n{row2}\n{row3}")
