from datetime import datetime
from enum import Enum
from faker import Faker


class Category(Enum):
    NOT_INFORMED = 0
    BEER = 1
    SODA = 2
    JUICE = 3
    WATER = 4


class Package:
    def __init__(self):
        self.name: str = ""

    def construct(self, name: str):
        self.name = name
        return self


class Order:
    def __init__(self):
        self.product_identifier: int = 0
        self.amount: int = 0

    def construct(self, product_identifier: int, amount: int):
        self.product_identifier = product_identifier
        self.amount = amount
        return self


class Product:
    def __init__(self):
        self.identifier: int = 0
        self.name: str = ""
        self.description: str = ""
        self.active: bool = False
        self.quantity_available: float = 0.0
        self.currency: tuple[float, str] = (0.0, "")
        self.orders: list[Order] = []
        self.locale_names: dict[str, str] = {}
        self.created_on = datetime.min
        self.category = Category.NOT_INFORMED
        self.package = None

    def construct(self,
                  identifier: int,
                  name: str,
                  description: str,
                  active: bool,
                  quantity_available: float,
                  currency: tuple[float, str],
                  orders: list[Order],
                  locale_names: dict[str, str],
                  created_on: datetime,
                  category: Category,
                  package: Package):
        self.identifier = identifier
        self.name = name
        self.description = description
        self.active = active
        self.quantity_available = quantity_available
        self.currency = currency
        self.orders = orders
        self.locale_names = locale_names
        self.created_on = created_on
        self.category = category
        self.package = package
        return self


def mock_product(faker: Faker):
    product_identifier = faker.pyint(min_value=1)

    countries = [faker.unique.country() for _ in range(faker.pyint(min_value=1, max_value=5))]
    locale_names = {}
    for country in countries:
        locale_names[country] = faker.name()

    return Product().construct(
        product_identifier,
        faker.name(),
        faker.sentence(),
        faker.pybool(),
        faker.pyfloat(min_value=0.1),
        (faker.pyfloat(min_value=0.1), faker.currency_code()),
        [mock_order(product_identifier, faker) for _ in range(faker.pyint(min_value=1, max_value=5))],
        locale_names,
        faker.date(),
        faker.enum(Category),
        Package().construct(faker.name()))


def mock_order(product_identifier: int, faker: Faker):
    return Order().construct(product_identifier, faker.pyint(min_value=1))

