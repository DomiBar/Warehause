def get_items(items):
    print("Nazwa\t Ilość\t Jednostka\t Cena jednostkowa")
    print(f"{'-'*len('Nazwa')}\t {'-'*len('Ilość')}\t {'-'*len('Jednostka')}\t {'-'*len('Cena jednostkowa')}\t")
    for i in range(len(items)):
        print(f"{items[i]['name']}\t {items[i]['quantity']}\t {items[i]['unit']}     \t {items[i]['unit_price']}")