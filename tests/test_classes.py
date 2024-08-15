from src.classes import Category, Product


def test_product_creation():
    product = Product("Test Product", "Test Description", 10.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 10.0
    assert product.quantity == 10


def test_category_creation():
    product1 = Product("Test Product1", "Test Description1", 10.0, 10)
    product2 = Product("Test Product2", "Test Description2", 20.0, 20)
    category = Category("Test Category", "Test Description", [product1, product2])
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert len(category.products) == 2
    assert category.products[0].name == "Test Product1"
    assert category.products[1].name == "Test Product2"


def test_category_product_count():
    Category.product_count = 0
    Category.category_count = 0
    product1 = Product("Test Product1", "Test Description1", 10.0, 10)
    product2 = Product("Test Product2", "Test Description2", 20.0, 20)
    Category("Test Category", "Test Description", [product1, product2])
    assert Category.product_count == 2
