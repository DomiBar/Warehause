import csv
from datetime import datetime

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

def sell_items(items, sold_items, product, sell_quantity, sell_price):
    for i in range(len(items)):
        if product==items[i]['name']:
            if sell_quantity<items[i]['quantity']:
                items[i]['quantity']-=sell_quantity
                print(f"Sprzedano {sell_quantity} {items[i]['unit']} {product}")
                now=datetime.now()
                now=now.strftime("%d/%m/%Y %H:%M:%S")
                sold_items.append({'name':product, 'quantity': sell_quantity, 'unit':items[i]['unit'], 'unit_price':sell_price, 'date':now})
                get_items(items)
                break
            else:
                print("Nie ma wystarczającej ilości produktu w magazynie")
                break
                
    else:
        print("Nie znaleziono podanego produktu w bazie")

def get_operations(sold_items):
    print("Data\t Nazwa\t Ilość\t Jednostka\t Cena jednostkowa")
    print(f"{'-'*len('Data')}\t {'-'*len('Nazwa')}\t {'-'*len('Ilość')}\t {'-'*len('Jednostka')}\t {'-'*len('Cena jednostkowa')}\t")
    for item in sold_items:
        print(f"{item['date']}\t {item['name']}\t {item['quantity']}\t {item['unit']}     \t {item['unit_price']}")

def get_costs(items):
    return sum([value['quantity']*value['unit_price'] for value in items])

def get_income(sold_items):
    return sum([value['quantity']*value['unit_price'] for value in sold_items])

def show_revenue(items, sold_items):
    print(f"Koszty: {get_costs(items)}")
    print(f"Przychody: {get_income(sold_items)}")
    print(f"Zysk: {get_income(sold_items)-get_costs(items)}")

def export_to_csv(items,sold_items):
    file_1='magazyn.csv'
    file_2='operations.csv'
    try:
        with open(file_1,'w', newline='') as csvfile:
            fieldnames=['name','quantity','unit','unit_price']
            writer=csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writerow({'name':'Nazwa','quantity':'Ilość','unit':'Jednostka','unit_price':'Cena jednostkowa'})
            writer.writerows(items)    
    except:
        print(f"!!!!!!Nie udało się otworzyć pliku {file_1} . Dane nie zostały zapisane.!!!!!!\nJeżeli plik jest otwarty w innym programie, zamknij go przed zapisem.")

    try:
        with open(file_2,'w', newline='') as csvfile:
            fieldnames=['date','name','quantity','unit','unit_price']
            writer=csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writerow({'name':'Nazwa','quantity':'Ilość','unit':'Jednostka','unit_price':'Cena jednostkowa','date':'Data'})
            writer.writerows(sold_items)    
    except:
        print(f"!!!!!!Nie udało się otworzyć pliku {file_1} . Dane nie zostały zapisane.!!!!!!\nJeżeli plik jest otwarty w innym programie, zamknij go przed zapisem.")

def load_from_csv(items,sold_items):
    file_1='magazyn.csv'
    file_2='operations.csv'
    with open(file_1, newline='') as csvfile:
        fieldnames=['name','quantity','unit','unit_price']
        reader=csv.DictReader(csvfile, fieldnames=fieldnames, delimiter=';')
        items.clear()
        for row in reader:
            if row['name']!='Nazwa':
                items.append(row)

    with open(file_2, newline='') as csvfile:
        fieldnames=['date','name','quantity','unit','unit_price']
        reader=csv.DictReader(csvfile, fieldnames=fieldnames, delimiter=';')
        sold_items.clear()
        for row in reader:
            if row['name']!='Nazwa':
                sold_items.append({'name':row['name'],'quantity':row['quantity'],'unit':row['unit'],'unit_price':row['unit_price'],'date':row['date']})