class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализирует новый экземпляр класса Product."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """Возвращает строковое представление экземпляра класса Product."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение стоимости товара."""
        if not isinstance(other, self.__class__):
            raise TypeError("Объект должен быть классом Product.")
        return self.__price * self.quantity + other.__price * other.quantity

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


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


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

    def __str__(self):
        """Возвращает строковое представление экземпляра класса Category."""
        sum_product = sum([product.quantity for product in self.__products])
        return f"{self.name}, количество продуктов: {sum_product} шт."

    def add_product(self, products):
        """Добавляет новый продукт в категорию."""
        if not isinstance(products, Product):
            raise TypeError("Объект должен быть классом Product.")
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


product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

print(str(product1))
print(str(product2))
print(str(product3))

category1 = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    [product1, product2, product3],
)

print(str(category1))

print(category1.products)

print(product1 + product2)
print(product1 + product3)
print(product2 + product3)
