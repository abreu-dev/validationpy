if __name__ == "__main__":
    from validationpy.results.validation_error import ValidationError

    error = ValidationError("Name", "Message", "Value")
    print(error.attempted_value)
