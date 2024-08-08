import random

direcao = {
    0: "Norte - N ⬆️",
    1: "Sudoeste - SO ↙️",
    2: "Sudeste - SE ↘️",
    3: "Oeste - O ⬅️",
    4: "Leste - L ➡️",
    5: "Noroeste - NO ↖️",
    6: "Nordeste - NE ↗️",
    7: "Sul - S ↙️"
}

dado = random.randint(0, 7)

print(f"\n    {direcao[dado]}") 
