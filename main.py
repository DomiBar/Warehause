import functions
import os

command=None
actions={1: "Wyjdź z programu",
         2: "Pokaż produkty",
         3: "Dodaj produkt",
         4: "Sprzedaj produkt",
         5: "Pokaż listę operacji",
         6: "Pokaż zysk",
         7: "Zapisz",
         8: "Importuj"
         }
items=[{'name':'dąb', 'quantity':11.00,'unit':'m3','unit_price':210.00},
       {'name':'buk', 'quantity':23.00,'unit':'m3','unit_price':180.00},
       {'name':'sosna', 'quantity':5.00,'unit':'m3','unit_price':140.00}
       ]
sold_items=[]
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
        functions.sell_items(items,sold_items,
                             input("Podaj nazwę produktu "), 
                             float(input("Podaj sprzedawaną ilość ")),
                             float(input("Podaj cenę sprzedaży "))
                            )
    if command==5:
        functions.get_operations(sold_items)
    if command==6:
        functions.show_revenue(items,sold_items)
    if command==7:
        functions.export_to_csv(items,sold_items)
    if command==8:
        functions.load_from_csv(items,sold_items)
    print()


print("Kończę działanie programu. Do widzenia.")