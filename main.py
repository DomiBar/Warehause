command=None
actions={1: "Wyjdź z programu",
         2: "Dodaj produkt"}

while command!=1:
    for action in actions:
        print(f"{action}. {actions[action]}")
    command=int(input("Co chcesz zrobić? "))

print("Kończę działanie programu. Do widzenia.")