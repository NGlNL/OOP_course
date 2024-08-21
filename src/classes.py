class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализирует новый экземпляр класса Product."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data):
        """Создает новый экземпляр класса Product на основе данных."""
        product = cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )
        return product

    @property
    def price(self):
        """Возвращает цену товара."""
        return self.__price

    @price.setter
    def price(self, price):
        """Устанавливает цену товара."""
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Инициализирует новый экземпляр класса Category."""
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(products)
        Category.category_count += 1

    def add_product(self, products):
        """Добавляет новый продукт в категорию."""
        self.__products.append(products)
        Category.product_count += 1

    @property
    def products(self):
        """Возвращает список продуктов в категории."""
        list_products = []
        for product in self.__products:
            product_string = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            list_products.append(product_string)
        return list_products

    def get_all_products(self):
        """Возвращает список объектов Product."""
        return self.__products
