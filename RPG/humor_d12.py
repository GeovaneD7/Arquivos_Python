import random

humor = {
    0: "Feliz - 😄",
    1: "Assustado(a) - 😨",
    2: "Galanteador(a) - 😘",
    3: "Brincalhão(ona) - 😆",
    4: "Confuso(a) - 😵‍💫",
    5: "Triste - 😞",
    6: "Apático(a) - 😒",
    7: "Encantado(a) - 🤩",
    8: "Irritado(a) - 😤",
    9: "Romântico(a) - 😍",
    10: "Interessado(a) - 🤔",
    11: "Hostil - 😡"
}

dado = random.randint(0, 11)

print(f"\n    {humor[dado]}") 
