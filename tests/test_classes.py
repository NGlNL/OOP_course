from src.classes import Category, LawnGrass, Product, Smartphone


def test_product_creation():
    product = Product("Test Product", "Test Description", 10.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 10.0
    assert product.quantity == 10


def test_create_category():
    product1 = Product("Smartphone", "Latest model", 599.99, 10)
    product2 = Product("Laptop", "High-performance laptop", 1199.99, 5)
    category = Category("Electronics", "Electronic devices and accessories", [product1, product2])
    assert category.name == "Electronics"
    assert category.description == "Electronic devices and accessories"
    assert len(category.get_all_products()) == 2


def test_category_product_count():
    Category.product_count = 0
    Category.category_count = 0
    product1 = Product("Test Product1", "Test Description1", 10.0, 10)
    product2 = Product("Test Product2", "Test Description2", 20.0, 20)
    Category("Test Category", "Test Description", [product1, product2])
    assert Category.product_count == 2


def test_category_add_product():
    Category.product_count = 0
    Category.category_count = 0
    product1 = Product.new_product(
        {"name": "Test Product1", "description": "Test Description1", "price": 10.0, "quantity": 10}
    )
    product2 = Product.new_product(
        {"name": "Test Product2", "description": "Test Description2", "price": 20.0, "quantity": 20}
    )
    category = Category("Test Category", "Test Description", [product1])
    category.add_product(product2)
    assert Category.product_count == 2
    assert len(category.products) == 2
    assert category.products[1] == f"{product2.name}, {product2.price} руб. Остаток: {product2.quantity} шт."


def test_category_get_all_products():
    product1 = Product.new_product(
        {"name": "Test Product1", "description": "Test Description1", "price": 10.0, "quantity": 10}
    )
    product2 = Product.new_product(
        {"name": "Test Product2", "description": "Test Description2", "price": 20.0, "quantity": 20}
    )
    category = Category("Test Category", "Test Description", [product1, product2])
    assert category.get_all_products() == [product1, product2]


def test_product_str():
    product = Product("Товар", "Описание товара", 100.0, 5)
    assert str(product) == "Товар, 100.0 руб. Остаток: 5 шт."


def test_product_add():
    product1 = Product("Товар1", "Описание товара1", 100.0, 5)
    product2 = Product("Товар2", "Описание товара2", 200.0, 10)
    assert product1 + product2 == 100.0 * 5 + 200.0 * 10


def test_category_str():
    Category.product_count = 0
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2],
    )
    assert str(category1) == "Смартфоны, количество продуктов: 13 шт."


def test_smartphone_initialization():
    smartphone = Smartphone(
        name="iPhone 14",
        description="Смартфон от Apple",
        price=99999.99,
        quantity=5,
        efficiency=90.0,
        model="iPhone 14",
        memory=128,
        color="черный",
    )

    assert smartphone.name == "iPhone 14"
    assert smartphone.description == "Смартфон от Apple"
    assert smartphone.price == 99999.99
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 90.0
    assert smartphone.model == "iPhone 14"
    assert smartphone.memory == 128
    assert smartphone.color == "черный"


def test_lawn_grass_initialization():
    lawn_grass = LawnGrass(
        name="Садовая трава",
        description="Трава для сада",
        price=499.99,
        quantity=10,
        country="Россия",
        germination_period="10 дней",
        color="зеленый",
    )

    assert lawn_grass.name == "Садовая трава"
    assert lawn_grass.description == "Трава для сада"
    assert lawn_grass.price == 499.99
    assert lawn_grass.quantity == 10
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "10 дней"
    assert lawn_grass.color == "зеленый"
