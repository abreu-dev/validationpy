if __name__ == "__main__":
    from validationpy.results.validation_error import ValidationError

    error = ValidationError("Name", "Message", None)
    print(error.attempted_value)
