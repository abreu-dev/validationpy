from dataclasses import dataclass
from datetime import datetime
from faker import Faker
from validationpy.results.validation_error import ValidationError
from validationpy.results.validation_result import ValidationResult


@dataclass
class Person:
    def __init__(self, name: str, birthday: datetime):
        self.name: str = name
        self.birthday: datetime = birthday


class Fixtures:
    def __init__(self):
        self.faker = Faker()

    def validation_error(self) -> ValidationError:
        return ValidationError(self.faker.word(), self.faker.sentence(), self.faker.word())

    def validation_result(self, many_errors: int = 0) -> ValidationResult:
        errors: list[ValidationError] = []

        for _ in range(0, many_errors, 1):
            errors.append(Fixtures.validation_error(self.faker))

        return ValidationResult(errors)

    def person(self) -> Person:
        return Person(self.faker.name(), self.faker.date_of_birth())
