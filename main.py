import functions
import os

command=None
actions={1: "Wyjdź z programu",
         2: "Pokaż produkty",
         3: "Dodaj produkt",
         4: "Sprzedaj produkt"
         }
items=[{'name':"dąb", 'quantity':11.00,"unit":'m3',"unit_price":210.00},
       {'name':"buk", 'quantity':23.00,"unit":'m3',"unit_price":180.00},
       {'name':"sosna", 'quantity':5.00,"unit":'m3',"unit_price":140.00}
       ]
while command!=1:
    for action in actions:
        print(f"{action}. {actions[action]}")
    command=int(input("Co chcesz zrobić? "))
    os.system("cls")
    if command==2:
        functions.get_items(items)
    if command==3:
        functions.add_items(items)
    if command==4:
        functions.sell_items(items,input("Podaj nazwę produktu "), float(input("Podaj sprzedawaną ilość ")))
    print()


print("Kończę działanie programu. Do widzenia.")