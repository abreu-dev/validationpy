from faker import Faker
from validationpy.results.validation_error import ValidationError
from validationpy.results.validation_result import ValidationResult


class Fixtures:
    def __init__(self, faker: Faker):
        self.faker = faker

    def validation_error(self):
        return ValidationError(self.faker.word(), self.faker.sentence(), self.faker.word())

    def validation_result(self, many_errors=0):
        errors = []

        for i in range(0, many_errors, 1):
            errors.append(Fixtures.validation_error(self.faker))

        return ValidationResult(errors)
