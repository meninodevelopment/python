from functools import partial

products = [
    {'name': 'Hamburguer', 'category': 'salgado', 'price': 7.5},
    {'name': 'Pastel', 'category': 'salgado', 'price': 5.0},
    {'name': 'Coca-cola', 'category': 'bebida', 'price': 9.5},
    {'name': 'Bolo', 'category': 'doce', 'price': 6.0},
    {'name': 'Torta Doce', 'category': 'doce', 'price': 6.0},
    {'name': 'Suco', 'category': 'bebida', 'price': 3.5},
    {'name': 'Mousse', 'category': 'doce', 'price': 4.0},
]

def apply_porcent(price, porcent):
    porcent = porcent if porcent >= 100 else 100 - porcent
    return price * (porcent / 100)



increase_in_ten = partial(apply_porcent, porcent=110)

products_with_increase = map(lambda p: {**p, p['price']: increase_in_ten(p['price'])})

print(*products_with_increase, sep='\n')