from faker import Faker
from unittest import TestCase, main
from validationpy.utils.attribute_chain import AttributeChain


class TestAttributeChain(TestCase):
    # region setUp
    def setUp(self) -> None:
        self.faker = Faker()
    # endregion

    # region __init__
    def test_init_should_set_attributes(self):
        # Act
        chain = AttributeChain()

        # Assert
        self.assertIsNotNone(chain.path_in_parts)
        self.assertFalse(chain.path_in_parts)

    def test_init_should_set_attributes_with_optional_parameters(self):
        # Arrange
        path_in_parts = self.faker.words(3)

        # Act
        chain = AttributeChain(path_in_parts)

        # Assert
        self.assertEqual(path_in_parts, chain.path_in_parts)
    # endregion

    # region __str__
    def test_str_should_return_custom(self):
        # Arrange
        path_in_parts = self.faker.words(3)
        chain = AttributeChain(path_in_parts)

        # Assert
        self.assertEqual(f'{path_in_parts[0]}.{path_in_parts[1]}.{path_in_parts[2]}', str(chain))
    # endregion

    # region from_lambda_expression
    def test_from_lambda_expression_should_create_chain(self):
        # Act
        chain = AttributeChain.from_lambda_expression(lambda x: x.product.currency.code)

        # Assert
        self.assertEqual(['product', 'currency', 'code'], chain.path_in_parts)
    # endregion


if __name__ == '__main__':
    main()
