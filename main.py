nombre = input("Cual es tu nombre?: ")
print("Hola", nombre)
edad = int(input("¿Cuantos años tienes? "))
if edad < 18:
    print("No puedes votar")
elif edad >= 18:
    print("Puedes votar")