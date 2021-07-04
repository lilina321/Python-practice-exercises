class Magazyn:

    def __init__(self, listOfProducts):
        self.listOfProducts = listOfProducts

    def display_products(self):
        print('Available products:')
        for product in self.listOfProducts:
            print(product)

    def add_product(self):
        self.nameOfProduct = input('Add product: >>> ')
        if self.nameOfProduct not in self.listOfProducts:
            self.listOfProducts.append(self.nameOfProduct)
            print(f'Product {self.nameOfProduct} was added.')
        else:
            print('Product already in stock')

    def remove_product(self):
        self.nameOfProduct = input('Remove product: >>> ')
        if self.nameOfProduct in self.listOfProducts:
            self.listOfProducts.remove(self.nameOfProduct)
            print(f'Product {self.nameOfProduct} was removed.')
        else:
            print('The specified product is not in stock.')


magazyn = Magazyn(['banana', 'apple', 'orange'])

print('''MENU MAGAZYN

Enter 1 to display products in stock.
Enter 2 to add product.
Enter 3 to remove product.
Enter 4 to exit.
''')
choice = ''
while choice != '4':
    choice = input('Enter number: ')
    if choice == '1':
        magazyn.display_products()
    elif choice == '2':
        magazyn.add_product()
    elif choice == '3':
        magazyn.remove_product()
        
    

