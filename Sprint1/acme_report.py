"""
Generate random products and print summary
"""

from acme import Product
from random import randint, sample, uniform

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    weight = randint(5, 101)
    price = randint(5, 101)
    flammability = uniform(0.0, 2.5)
    products = []
    while num_products > 0:
        adj = ADJECTIVES[randint(0, (len(ADJECTIVES)) - 1)]
        noun = NOUNS[randint(0, (len(NOUNS)) - 1)]
        name = f'{adj} ' \
               f'{noun}'
        rnd_sample = Product(name=name,
                             price=price,
                             weight=weight,
                             flammability=flammability
                             )
        products.append(rnd_sample)
        num_products -= 1
    return products


def inventory_report(products):
    u_names = set()
    l_price = []
    l_weight = []
    l_flame = []
    test_samples = len(products) - 1
    while test_samples > -1:
        u_names.add(products[test_samples].name)
        l_weight.append(products[test_samples].weight)
        l_price.append(products[test_samples].price)
        l_flame.append(products[test_samples].flammability)
        test_samples -= 1
    print(f'Unique product name: {len(u_names)}\n'
          f'Average price: {sum(l_price) / len(l_price)}\n'
          f'Average weight: {sum(l_weight) / len(l_weight)}\n'
          f'Average flammability: {sum(l_flame) / len(l_flame)}'
          )


if __name__ == '__main__':
    inventory_report(generate_products())