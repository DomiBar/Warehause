def get_items(items):
    print("Nazwa\t Ilość\t Jednostka\t Cena jednostkowa")
    print(f"{'-'*len('Nazwa')}\t {'-'*len('Ilość')}\t {'-'*len('Jednostka')}\t {'-'*len('Cena jednostkowa')}\t")
    sort_items(items)
    for i in range(len(items)):
        print(f"{items[i]['name']}\t {items[i]['quantity']}\t {items[i]['unit']}     \t {items[i]['unit_price']}")

def add_items(items):
    name=input("Podaj nazwę produktu: ")
    quantity=float(input("Podaj ilość: "))
    unit_name=input("Podaj nazwę jednostki: ")
    unit_price=float(input("Podaj cenę jednostkową: "))
    items+=[{'name':name, 'quantity':quantity,"unit":unit_name,"unit_price":unit_price}]
    
def sort_items(items):
    dict_temp={}
    for i in range(1,len(items)):
        while items[-i]["name"]<items[-i-1]["name"]:
            dict_temp=items[-i-1]
            items[-i-1]=items[-i]
            items[-i]=dict_temp