items = [
    {
        "product": "camisa",
        "price": 100
    },
    {
        "product": "pantalon",
        "price": 200
    },
    {
        "product": "pantalon 2",
        "price": 300
    }
]
prices = list(map(lambda item : item["price"], items))
print(prices) 

def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .19
    return new_item

#add taxes es la función que va a ejecutar y items es la var que va a tomar
new_items = list(map(add_taxes, items))
print(new_items)

print(items)