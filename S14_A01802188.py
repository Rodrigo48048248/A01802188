#Ejercicio 1
edad = int(input("¿Cuál es tu edad? "))

if edad >= 18:
    print("Eres adulto.")
else:
    print("No eres adulto.")

#Ejercicio 2
edad = int(input("¿Cuál es tu edad? "))

if 13 <= edad <= 19:
    print("Eres adolescente.")
else:
    print("No eres adolescente.")

#Ejercicio 3
Fechan = int(input("¿En qué año naciste? "))
total = 2025 - Fechan
print(f"tienes {total}")
