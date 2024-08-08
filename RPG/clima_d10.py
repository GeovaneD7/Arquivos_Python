import random

clima = {
    0: "Ensolarado - ☀️",
    1: "Nublado - ☁️",
    2: "Quente - 🔥",
    3: "Ventando - 🌬️",
    4: "Tempestade com trovões - ⛈️",
    5: "Frio - ❄️",
    6: "Chuvoso - 🌧️",
    7: "Neve/Granizo - 🌨️",
    8: "Parcialmente Nublado - ⛅",
    9: "Chuva Esparsa - 🌦️"
}

dado = random.randint(0, 9)

print(f"\n    {clima[dado]}") 
