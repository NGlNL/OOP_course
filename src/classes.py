from abc import ABC, abstractmethod


class MixinLog:
    """Миксин для логирования"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_name = self.__class__.__name__
        params = ", ".join(f"{arg}" for arg in args)
        print(f"{class_name} создан с параметрами:{params}")


class BaseProduct(ABC):
    """Абстрактный класс"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен.")
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
    @abstractmethod
    def new_product(cls, product_data: dict, existing_products: list):
        """Создает новый экземпляр класса Product на основе данных."""
        pass

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

    @abstractmethod
    def update_quantity(self, quantity: int):
        """Изменяет количество товара."""
        pass

    @abstractmethod
    def delete_product(self):
        pass


class Product(MixinLog, BaseProduct):

    @classmethod
    def new_product(cls, product_data: dict, existing_products: list):
        for existing_product in existing_products:
            if existing_product.name == product_data["name"]:
                existing_product.quantity += product_data["quantity"]
                existing_product.price = min(existing_product.price, product_data["price"])
                return existing_product

        return cls(product_data["name"], product_data["description"], product_data["price"], product_data["quantity"])

    def update_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Количество должно быть неотрицательным целым числом")
        self.quantity = quantity

    def delete_product(self):
        self.quantity = 0


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

    def middle_price(self) -> float:
        """Возвращает среднюю цену продуктов в категории."""
        try:
            total_price = sum(product.price * product.quantity for product in self.__products)
            total_quantity = sum(product.quantity for product in self.__products)
            average = total_price / total_quantity
        except ZeroDivisionError:
            print("На ноль делить нельзя")
            return 0
        return round(average, 2)

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
