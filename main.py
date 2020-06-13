import functions

command=None
actions={1: "Wyjdź z programu",
         2: "Pokaż produkty"
         }
items=[{'name':"buk", 'quantity':23,"unit":'m3',"unit_price":180},
       {'name':"dąb", 'quantity':11,"unit":'m3',"unit_price":210},
       {'name':"sosna", 'quantity':5,"unit":'m3',"unit_price":140}
       ]
while command!=1:
    for action in actions:
        print(f"{action}. {actions[action]}")
    command=int(input("Co chcesz zrobić? "))
    if command==2:
        functions.get_items(items)

print("Kończę działanie programu. Do widzenia.")